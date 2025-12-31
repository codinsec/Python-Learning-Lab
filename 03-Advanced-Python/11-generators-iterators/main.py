# Generators and Iterators in Python

print("=== Basic Generator Function ===")

def countdown(n):
    """Generator function that counts down from n to 1"""
    while n > 0:
        yield n
        n -= 1

# Generator doesn't execute until iterated
counter = countdown(5)
print(f"Counter object: {counter}")
print(f"Is generator: {hasattr(counter, '__iter__')}")

# Execute generator
print("Countdown:")
for num in counter:
    print(f"  {num}")

print("\n=== Generator vs List ===")

# List (eager evaluation - all values in memory)
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator (lazy evaluation - values generated on demand)
def squares_generator(n):
    for i in range(n):
        yield i ** 2

# List uses memory for all values
squares = squares_list(5)
print(f"Squares list: {squares}")

# Generator uses memory only for current value
squares_gen = squares_generator(5)
print(f"Squares generator: {squares_gen}")
print(f"Squares from generator: {list(squares_gen)}")

print("\n=== Generator Expression ===")

# Generator expression (similar to list comprehension)
squares_gen_expr = (x ** 2 for x in range(5))
print(f"Generator expression: {squares_gen_expr}")
print(f"Values: {list(squares_gen_expr)}")

# Memory efficient for large datasets
large_gen = (x * 2 for x in range(1000000))
print(f"Large generator created (no memory used yet): {large_gen}")

print("\n=== Infinite Generator ===")

def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("First 10 Fibonacci numbers:")
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(f"  {num}")

print("\n=== Custom Iterator Class ===")

class CountUp:
    """Custom iterator class"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 6)
print("Custom iterator:")
for num in counter:
    print(f"  {num}")

print("\n=== Generator Pipeline ===")

def numbers():
    """Generate numbers"""
    n = 1
    while True:
        yield n
        n += 1

def square(nums):
    """Square numbers"""
    for num in nums:
        yield num ** 2

def filter_even(nums):
    """Filter even numbers"""
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators
pipeline = filter_even(square(numbers()))
print("First 5 even squares:")
for i, num in enumerate(pipeline):
    if i >= 5:
        break
    print(f"  {num}")

print("\n=== Generator State ===")

def stateful_generator():
    """Generator that maintains state"""
    value = 0
    while True:
        received = yield value
        if received is not None:
            value = received
        else:
            value += 1

gen = stateful_generator()
print(f"Initial value: {next(gen)}")
print(f"Next value: {next(gen)}")
print(f"Send value 10: {gen.send(10)}")
print(f"Next value: {next(gen)}")

print("\n=== Generator with Multiple Yields ===")

def multi_yield():
    """Generator with multiple yield points"""
    yield "First"
    yield "Second"
    yield "Third"

gen = multi_yield()
print("Multiple yields:")
for value in gen:
    print(f"  {value}")

print("\n=== Generator for File Reading ===")

def read_lines(filename):
    """Generator to read file line by line (memory efficient)"""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        yield f"File {filename} not found"

# Example usage (would work with actual file)
print("File reading generator created")

print("\n=== Generator for Pagination ===")

def paginate(items, page_size):
    """Generator that yields pages of items"""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

items = list(range(1, 21))
print(f"Items: {items}")
print("Pages (size 5):")
for page_num, page in enumerate(paginate(items, 5), 1):
    print(f"  Page {page_num}: {page}")

