import threading
from functools import wraps

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls):
    _instances = {}
    _lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:                 # First check (no lock)
            with _lock:
                if cls not in _instances:         # Second check (with lock)
                    _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper


@singleton
class AppConfig:
    def __init__(self):
        print("AppConfig initialized")

