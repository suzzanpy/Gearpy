import time
from functools import wraps
from concurrent.futures import ThreadPoolExecutor

def optimize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(func, *args, **kwargs)
            return future.result()
    return wrapper
