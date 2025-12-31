# Decorators and Closures in Python

import functools
import time

print("=== Closures ===")

def outer_function(x):
    """Outer function that returns inner function (closure)"""
    def inner_function(y):
        # Inner function has access to outer function's variables
        return x + y
    return inner_function

# Create closure
add_five = outer_function(5)
print(f"add_five(3): {add_five(3)}")
print(f"add_five(10): {add_five(10)}")

# Another closure example
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

print("\n=== Basic Decorator ===")

def my_decorator(func):
    """Simple decorator that adds functionality"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\n=== Decorator with Arguments ===")

def repeat(times):
    """Decorator factory that returns a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Python")

print("\n=== Decorator Preserving Metadata ===")

def simple_decorator(func):
    """Decorator without functools.wraps"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

def better_decorator(func):
    """Decorator with functools.wraps"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def function1():
    """Original function 1"""
    pass

@better_decorator
def function2():
    """Original function 2"""
    pass

print(f"function1 name: {function1.__name__}")
print(f"function1 doc: {function1.__doc__}")
print(f"function2 name: {function2.__name__}")
print(f"function2 doc: {function2.__doc__}")

print("\n=== Timing Decorator ===")

def timing_decorator(func):
    """Decorator that measures function execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Function that takes some time"""
    time.sleep(0.1)
    return "Done"

result = slow_function()
print(f"Result: {result}")

print("\n=== Decorator with Arguments (Advanced) ===")

def retry(max_attempts=3):
    """Decorator that retries function on failure"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_function(value):
    """Function that might fail"""
    if value < 0:
        raise ValueError("Value must be positive")
    return value * 2

print(f"risky_function(5): {risky_function(5)}")
# risky_function(-1)  # Would retry 3 times then raise

print("\n=== Class-Based Decorator ===")

class CountCalls:
    """Decorator class that counts function calls"""
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()

print("\n=== Decorator Chaining ===")

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello, World!"

print(f"Decorated text: {get_text()}")

print("\n=== Decorator with State ===")

def cache(func):
    """Decorator that caches function results"""
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]
    return wrapper

@cache
def expensive_function(n):
    """Expensive computation"""
    print(f"Computing for {n}...")
    return n ** 2

print(f"First call: {expensive_function(5)}")
print(f"Second call (cached): {expensive_function(5)}")
print(f"Different argument: {expensive_function(6)}")

print("\n=== Property-Like Decorator ===")

def validate_positive(func):
    """Decorator that validates function arguments are positive"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(f"Area (5, 3): {calculate_area(5, 3)}")
# calculate_area(-5, 3)  # Would raise ValueError

