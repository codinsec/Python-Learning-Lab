# Variables and Data Types in Python

# Python uses dynamic typing - no need to declare types
name = "Python"
age = 30
height = 5.9
is_student = True
has_car = None

print("=== Variable Examples ===")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Has Car: {has_car}, Type: {type(has_car)}")

# Variable naming follows snake_case (PEP 8)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nFull Name: {full_name}")

# Type conversion (casting)
number_str = "42"
number_int = int(number_str)
number_float = float(number_str)

print("\n=== Type Conversion ===")
print(f"String '42' converted to int: {number_int}")
print(f"String '42' converted to float: {number_float}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Swapping variables (Pythonic way)
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Constants (convention: UPPER_CASE)
MAX_SIZE = 100
PI = 3.14159
print(f"\nConstants: MAX_SIZE={MAX_SIZE}, PI={PI}")

