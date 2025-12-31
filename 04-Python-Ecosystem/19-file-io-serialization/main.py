# File I/O and Serialization in Python

import json
import pickle
import csv
import os
from pathlib import Path

print("=== Basic File Writing ===")

# Write text file
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    f.write("Python file I/O example.")

print("File written: example.txt")

# Read text file
with open("example.txt", "r") as f:
    content = f.read()
    print(f"File content:\n{content}")

# Read line by line
print("\nReading line by line:")
with open("example.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

# Clean up
os.remove("example.txt")

print("\n=== File Modes ===")

file_modes = {
    "r": "Read (text, file must exist)",
    "w": "Write (text, creates/overwrites)",
    "a": "Append (text, creates if doesn't exist)",
    "r+": "Read and write (text)",
    "rb": "Read (binary)",
    "wb": "Write (binary)",
    "ab": "Append (binary)"
}

print("Common file modes:")
for mode, description in file_modes.items():
    print(f"  '{mode}': {description}")

print("\n=== JSON Serialization ===")

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "Istanbul",
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True
}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON file written: data.json")

# Read JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(f"Loaded data: {loaded_data}")

# JSON string serialization
json_string = json.dumps(data, indent=2)
print(f"\nJSON string:\n{json_string}")

# Deserialize from string
parsed_data = json.loads(json_string)
print(f"Parsed from string: {parsed_data['name']}")

# Clean up
os.remove("data.json")

print("\n=== JSON with Custom Objects ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def to_dict(self):
        return {"name": self.name, "age": self.age}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

person = Person("Bob", 25)

# Serialize custom object
person_dict = person.to_dict()
with open("person.json", "w") as f:
    json.dump(person_dict, f, indent=2)

# Deserialize
with open("person.json", "r") as f:
    person_data = json.load(f)
    restored_person = Person.from_dict(person_data)
    print(f"Restored person: {restored_person.name}, {restored_person.age}")

# Clean up
os.remove("person.json")

print("\n=== Pickle Serialization ===")

# Pickle can serialize Python objects directly
class ComplexObject:
    def __init__(self, value):
        self.value = value
        self.data = [1, 2, 3, 4, 5]
    
    def __repr__(self):
        return f"ComplexObject(value={self.value}, data={self.data})"

obj = ComplexObject(42)

# Serialize with pickle (binary)
with open("object.pkl", "wb") as f:
    pickle.dump(obj, f)

print("Object pickled: object.pkl")

# Deserialize
with open("object.pkl", "rb") as f:
    loaded_obj = pickle.load(f)
    print(f"Loaded object: {loaded_obj}")

# Pickle to bytes
pickled_bytes = pickle.dumps(obj)
print(f"Pickled to bytes: {len(pickled_bytes)} bytes")

# Unpickle from bytes
unpickled_obj = pickle.loads(pickled_bytes)
print(f"Unpickled object: {unpickled_obj}")

# Clean up
os.remove("object.pkl")

print("\n=== CSV File Operations ===")

# Write CSV file
data_rows = [
    ["Name", "Age", "City"],
    ["Alice", 30, "Istanbul"],
    ["Bob", 25, "Ankara"],
    ["Charlie", 35, "Izmir"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_rows)

print("CSV file written: people.csv")

# Read CSV file
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    print("CSV content:")
    for row in reader:
        print(f"  {row}")

# Read as dictionary
with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    print("\nCSV as dictionary:")
    for row in reader:
        print(f"  {row}")

# Clean up
os.remove("people.csv")

print("\n=== CSV with Custom Delimiters ===")

# Write with semicolon delimiter
with open("data_semicolon.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Name", "Value"])
    writer.writerow(["Item1", 100])
    writer.writerow(["Item2", 200])

# Read with semicolon delimiter
with open("data_semicolon.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    print("Semicolon-delimited CSV:")
    for row in reader:
        print(f"  {row}")

# Clean up
os.remove("data_semicolon.csv")

print("\n=== File Path Operations ===")

# Using pathlib (modern approach)
file_path = Path("example_file.txt")

# Write using pathlib
file_path.write_text("Content from pathlib")

# Read using pathlib
content = file_path.read_text()
print(f"Content from pathlib: {content}")

# Path operations
print(f"File name: {file_path.name}")
print(f"File stem: {file_path.stem}")
print(f"File suffix: {file_path.suffix}")
print(f"Parent directory: {file_path.parent}")

# Check if file exists
print(f"File exists: {file_path.exists()}")

# Clean up
file_path.unlink()

print("\n=== Binary File Operations ===")

# Write binary data
binary_data = b"Hello, Binary World!"
with open("binary_file.bin", "wb") as f:
    f.write(binary_data)

# Read binary data
with open("binary_file.bin", "rb") as f:
    loaded_binary = f.read()
    print(f"Binary data: {loaded_binary}")

# Clean up
os.remove("binary_file.bin")

print("\n=== Appending to Files ===")

# Append mode
with open("append_example.txt", "w") as f:
    f.write("First line\n")

with open("append_example.txt", "a") as f:
    f.write("Second line (appended)\n")
    f.write("Third line (appended)\n")

# Read appended content
with open("append_example.txt", "r") as f:
    print("Appended content:")
    print(f.read())

# Clean up
os.remove("append_example.txt")

print("\n=== Error Handling ===")

def safe_read_file(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

result = safe_read_file("nonexistent.txt")
print(f"Safe read result: {result}")

print("\n=== Working with Directories ===")

# Create directory
test_dir = Path("test_directory")
test_dir.mkdir(exist_ok=True)

# Create file in directory
test_file = test_dir / "test.txt"
test_file.write_text("Test content")

# List directory contents
print(f"Directory contents: {list(test_dir.iterdir())}")

# Clean up
test_file.unlink()
test_dir.rmdir()

print("\n=== JSON with Lists and Nested Data ===")

complex_data = {
    "users": [
        {"id": 1, "name": "Alice", "roles": ["admin", "user"]},
        {"id": 2, "name": "Bob", "roles": ["user"]}
    ],
    "metadata": {
        "version": "1.0",
        "created": "2024-01-01"
    }
}

with open("complex.json", "w") as f:
    json.dump(complex_data, f, indent=2)

with open("complex.json", "r") as f:
    loaded = json.load(f)
    print(f"Users count: {len(loaded['users'])}")
    print(f"First user: {loaded['users'][0]['name']}")

# Clean up
os.remove("complex.json")

print("\n=== Best Practices ===")

best_practices = [
    "Always use context managers (with statement) for file operations",
    "Handle file errors with try/except",
    "Use appropriate file modes (r, w, a, etc.)",
    "Use JSON for data exchange with other systems",
    "Use Pickle only for Python-to-Python serialization",
    "Be careful with Pickle - only unpickle trusted sources",
    "Use pathlib for modern path operations",
    "Close files explicitly or use context managers",
    "Handle encoding for text files (UTF-8 by default)"
]

print("File I/O best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

