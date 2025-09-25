from kivy.resources import resource_find

def asset(path: str) -> str:
    """Return a safe absolute path to an asset or raise if missing."""
    p = resource_find(path)
    if not p:
        raise FileNotFoundError(f"Asset not found: {path}")
    return p
