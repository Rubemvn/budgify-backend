from threading import Lock

_blacklist_set = set()
_lock = Lock()

def is_blacklisted(jti: str) -> bool:
    return jti in _blacklist_set

def add_to_blacklist(jti: str):
    global _blacklist_set
    with _lock:
        _blacklist_set.add(jti)
