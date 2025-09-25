import json
from pathlib import Path

def load_local_json(rel_path: str) -> dict:
    p = Path(rel_path)
    return json.loads(p.read_text(encoding="utf-8"))