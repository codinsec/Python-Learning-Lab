# Lists, Tuples, Sets, and Dictionaries in Python

print("=== LISTS ===")

# List creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# List indexing and slicing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slicing [1:3]: {fruits[1:3]}")

# List methods
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "grape")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

fruits.extend(["kiwi", "mango"])
print(f"After extend: {fruits}")

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

print("\n=== TUPLES ===")

# Tuple creation (immutable)
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")

# Tuple unpacking
x, y = coordinates
name, age, job = person

print(f"X: {x}, Y: {y}")
print(f"Name: {name}, Age: {age}, Job: {job}")

# Tuple as return value
def get_name_age():
    return "Bob", 25

name, age = get_name_age()
print(f"Returned: {name}, {age}")

# Single element tuple (note the comma)
single = (42,)
print(f"Single element tuple: {single}")

print("\n=== SETS ===")

# Set creation (unique elements)
colors = {"red", "green", "blue", "red"}  # Duplicate removed
print(f"Colors: {colors}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set methods
set1.add(6)
print(f"After add: {set1}")

set1.remove(1)
print(f"After remove: {set1}")

# Set comprehension
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(f"Even numbers set: {even_set}")

print("\n=== DICTIONARIES ===")

# Dictionary creation
person = {
    "name": "Alice",
    "age": 30,
    "city": "Istanbul"
}

print(f"Person: {person}")

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Email: {person.get('email', 'Not provided')}")

# Adding/updating
person["email"] = "alice@example.com"
person["age"] = 31

print(f"Updated: {person}")

# Dictionary methods
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Iterating
print("\nDictionary iteration:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Nested dictionary
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

print(f"\nStudents: {students}")
print(f"Alice's grade: {students['alice']['grade']}")

print("\n=== NESTED STRUCTURES ===")

# List of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28}
]

print("People list:")
for person in people:
    print(f"  {person['name']}: {person['age']}")

# Dictionary with lists
classroom = {
    "math": ["Alice", "Bob"],
    "science": ["Charlie", "Alice"],
    "english": ["Bob", "Charlie"]
}

print(f"\nClassroom: {classroom}")
print(f"Math students: {classroom['math']}")

