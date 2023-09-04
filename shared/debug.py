

def debug_time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time {func.__name__}: {end - start}")
    return wrapper
