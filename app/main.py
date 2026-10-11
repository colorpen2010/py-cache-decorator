from typing import Callable, Any, Dict, Tuple

def cache(func: Callable) -> Callable:
    # Each decorated function gets its own cache dictionary
    cache_storage: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args, **kwargs):
        # Create a key from both positional and keyword arguments
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
