from functools import wraps

# Write a decorator that returns the function name 
def log_call(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(fn(*args, **kwargs))
    return wrapper

@log_call
def add_num(x, y):
    return x+y

add_num(3,4)

# Write a decorator that print the decorated function in n times
def repeat_fxn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Hello Ola"*fn(*args))
    return wrapper

@repeat_fxn
def repeater(n):
    return n

repeater(2)