from dataclasses import dataclass
from typing import Optional, Dict
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
import base64, os, hmac, hashlib, configparser, pathlib



# ---- Password hashing (portable, no native wheels needed) ----
PBKDF_ALGO = "sha256"
PBKDF_ITER = 200_000
SALT_LEN = 16
KEY_LEN = 32

def _pbkdf_hash(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(PBKDF_ALGO, password.encode("utf-8"), salt, PBKDF_ITER, dklen=KEY_LEN)

def hash_password(password: str) -> Dict[str, str]:
    salt = os.urandom(SALT_LEN)
    dk = _pbkdf_hash(password, salt)
    return {
        "algo": "pbkdf2",
        "hash": base64.b64encode(dk).decode(),
        "salt": base64.b64encode(salt).decode(),
        "iter": str(PBKDF_ITER),
        "digest": PBKDF_ALGO,
    }

def verify_password(password: str, stored: Dict[str, str]) -> bool:
    if stored.get("algo") != "pbkdf2":
        return False
    salt = base64.b64decode(stored["salt"])
    expected = base64.b64decode(stored["hash"])
    test = _pbkdf_hash(password, salt)
    return hmac.compare_digest(test, expected)

# ---- Config loader ----
def _read_db_config():
    cfg = configparser.ConfigParser()
    cfg_path = pathlib.Path("config/config.ini")
    if not cfg_path.exists():
        raise FileNotFoundError("config/config.ini not found. Create it with [db] uri and name.")
    cfg.read(cfg_path)
    uri = cfg.get("db", "uri", fallback=None)
    name = cfg.get("db", "name", fallback=None)
    if not uri or not name:
        raise ValueError("config.ini missing [db] uri or name")
    return uri, name

@dataclass
class AuthService:
    client: MongoClient
    db_name: str

    @classmethod
    def from_config(cls) -> "AuthService":
        uri, name = _read_db_config()
        client = MongoClient(uri, retryWrites=True, uuidRepresentation="standard")
        svc = cls(client=client, db_name=name)
        svc._ensure_indexes()
        return svc

    # Collections
    @property
    def users(self):
        return self.client[self.db_name]["users"]

    def _ensure_indexes(self):
        # unique on username and email
        self.users.create_index([("username", ASCENDING)], unique=True)
        self.users.create_index([("email", ASCENDING)], unique=True, sparse=True)

    # --- API ---
    def register_user(self, *, username: str, email: Optional[str], password: str) -> str:
        doc = {
            "username": username.strip().lower(),
            "email": (email or "").strip().lower() or None,
            "password": hash_password(password),
            "is_active": True,
        }
        try:
            res = self.users.insert_one(doc)
            return str(res.inserted_id)
        except DuplicateKeyError as e:
            # Decide which field duped
            key = "username" if "username" in str(e) else "email"
            raise ValueError(f"{key.capitalize()} already exists")

    def verify_user(self, *, identifier: str, password: str) -> Optional[Dict]:
        """identifier can be username or email"""
        q = {"$or": [
            {"username": identifier.strip().lower()},
            {"email": identifier.strip().lower()},
        ]}
        user = self.users.find_one(q, {"_id": 0, "username": 1, "email": 1, "password": 1, "is_active": 1})
        if not user or not user.get("is_active", True):
            return None
        if verify_password(password, user["password"]):
            return {"username": user["username"], "email": user.get("email")}
        return None
