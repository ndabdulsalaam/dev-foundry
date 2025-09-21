import time
from functools import wraps

def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        run_program = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"The program took {end_time - start_time:.2f} second(s)")
    return wrapper

@timed
def program_time(n: int):
    time.sleep(n)

program_time("5")

# Define decorate with dictionary unpacking
DEFAULTS = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "timeout": 30,
}

def build_config(**kwargs):
    return {**DEFAULTS, **kwargs}

new_dict = build_config(port=9090, debug=True)
print(new_dict)