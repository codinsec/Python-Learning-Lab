# Functions and Lambda in Python

print("=== Basic Functions ===")

# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

# Function with default parameters
def introduce(name, age=25, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}"

print(introduce("Alice"))
print(introduce("Bob", 30))
print(introduce("Charlie", 35, "Istanbul"))

# Function with keyword arguments
print("\n=== Keyword Arguments ===")
def create_profile(name, age, email):
    return f"Name: {name}, Age: {age}, Email: {email}"

# Can call with keyword arguments in any order
print(create_profile(email="test@example.com", name="John", age=28))

# *args - variable positional arguments
print("\n=== *args (Variable Positional Arguments) ===")
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_numbers(10, 20, 30, 40)}")

def print_info(*args):
    print("Arguments received:", args)
    for arg in args:
        print(f"  - {arg}")

print_info("Python", "is", "awesome")

# **kwargs - variable keyword arguments
print("\n=== **kwargs (Variable Keyword Arguments) ===")
def print_user_info(**kwargs):
    print("User information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_user_info(name="Alice", age=30, city="New York", occupation="Developer")

# Combining *args and **kwargs
print("\n=== Combining *args and **kwargs ===")
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="John", age=25)

# Lambda functions (anonymous functions)
print("\n=== Lambda Functions ===")

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"Add 10 and 20: {add(10, 20)}")

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Sort with lambda
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_by_age = sorted(students, key=lambda student: student[1])
print(f"Sorted by age: {sorted_by_age}")

# Function scope
print("\n=== Function Scope ===")
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")

