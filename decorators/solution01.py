import time
## BASIC CONCEPT OF DECORATOR IS WE NEED TO MAKE FUNCTION INSIDE A FUNCTION.
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)