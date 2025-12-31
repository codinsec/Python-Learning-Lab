# Magic Methods (Dunder Methods) in Python

print("=== String Representation ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        """Developer-friendly string representation"""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)
print(f"str(person): {str(person)}")
print(f"repr(person): {repr(person)}")
print(f"person: {person}")  # Uses __str__

print("\n=== Comparison Operators ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Less than comparison (based on distance from origin)"""
        if isinstance(other, Point):
            return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
        return NotImplemented
    
    def __le__(self, other):
        """Less than or equal"""
        return self < other or self == other
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 < p3: {p1 < p3}")

print("\n=== Arithmetic Operators ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Addition operator"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction operator"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Multiplication by scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right multiplication (scalar * vector)"""
        return self * scalar
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"v1 + v2: {v1 + v2}")
print(f"v2 - v1: {v2 - v1}")
print(f"v1 * 3: {v1 * 3}")
print(f"2 * v1: {2 * v1}")

print("\n=== Type Conversion ===")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __int__(self):
        """Convert to integer"""
        return int(self.celsius)
    
    def __float__(self):
        """Convert to float"""
        return float(self.celsius)
    
    def __bool__(self):
        """Convert to boolean"""
        return self.celsius != 0
    
    def __str__(self):
        return f"{self.celsius}°C"

temp = Temperature(25.7)
print(f"int(temp): {int(temp)}")
print(f"float(temp): {float(temp)}")
print(f"bool(temp): {bool(temp)}")
print(f"bool(Temperature(0)): {bool(Temperature(0))}")

print("\n=== Container Methods ===")

class ShoppingList:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        """Return length"""
        return len(self.items)
    
    def __getitem__(self, index):
        """Get item by index"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Set item by index"""
        self.items[index] = value
    
    def __delitem__(self, index):
        """Delete item by index"""
        del self.items[index]
    
    def __contains__(self, item):
        """Check if item is in list"""
        return item in self.items
    
    def append(self, item):
        self.items.append(item)
    
    def __repr__(self):
        return f"ShoppingList({self.items})"

shopping = ShoppingList()
shopping.append("Milk")
shopping.append("Bread")
shopping.append("Eggs")

print(f"Shopping list: {shopping}")
print(f"Length: {len(shopping)}")
print(f"First item: {shopping[0]}")
print(f"'Milk' in list: {'Milk' in shopping}")
print(f"'Butter' in list: {'Butter' in shopping}")

shopping[1] = "Butter"
print(f"After update: {shopping}")

del shopping[0]
print(f"After deletion: {shopping}")

print("\n=== Callable Objects ===")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        """Make object callable"""
        return value * self.factor
    
    def __repr__(self):
        return f"Multiplier({self.factor})"

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

# Can use in map, filter, etc.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(f"Doubled numbers: {doubled}")

print("\n=== Attribute Access ===")

class AttributeLogger:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        """Called when attribute is not found"""
        print(f"Getting attribute: {name}")
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        """Called when setting attribute"""
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print(f"Setting attribute: {name} = {value}")
            if not hasattr(self, '_data'):
                super().__setattr__('_data', {})
            self._data[name] = value
    
    def __delattr__(self, name):
        """Called when deleting attribute"""
        print(f"Deleting attribute: {name}")
        if name in self._data:
            del self._data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

obj = AttributeLogger()
obj.name = "Alice"
print(f"obj.name: {obj.name}")
del obj.name

print("\n=== Context Manager Methods ===")

class Timer:
    def __init__(self, name):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"{self.name} started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start_time
        print(f"{self.name} completed in {elapsed:.4f} seconds")
        return False
    
    def elapsed(self):
        import time
        if self.start_time:
            return time.time() - self.start_time
        return 0

with Timer("Operation") as timer:
    import time
    time.sleep(0.1)

print("\n=== Hash and Equality ===")

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
    def __hash__(self):
        """Make object hashable (required for use in sets/dicts)"""
        return hash(self.student_id)
    
    def __repr__(self):
        return f"Student({self.student_id}, '{self.name}')"

student1 = Student(1, "Alice")
student2 = Student(1, "Alice")
student3 = Student(2, "Bob")

print(f"student1 == student2: {student1 == student2}")
print(f"student1 == student3: {student1 == student3}")

# Can use in sets (requires __hash__)
students = {student1, student2, student3}
print(f"Students set: {students}")

