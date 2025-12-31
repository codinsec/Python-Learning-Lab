# Classes and Objects in Python

print("=== Basic Class Definition ===")

class Person:
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    # Constructor method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old"

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())

# Accessing instance variables
print(f"\nPerson1 name: {person1.name}")
print(f"Person2 age: {person2.age}")

# Accessing class variable
print(f"Species: {Person.species}")
print(f"Person1 species: {person1.species}")

# Modifying instance variables
person1.age = 26
print(f"\nUpdated Person1 age: {person1.age}")

# Calling methods
print(person1.have_birthday())

print("\n=== Class Methods and Static Methods ===")

class Calculator:
    # Class variable
    pi = 3.14159
    
    def __init__(self, name):
        self.name = name
    
    # Instance method
    def add(self, a, b):
        return a + b
    
    # Class method (takes cls as first parameter)
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    @classmethod
    def create_default(cls):
        return cls("Default Calculator")
    
    # Static method (no self or cls)
    @staticmethod
    def multiply(a, b):
        return a * b

calc = Calculator("My Calculator")
print(f"Calculator name: {calc.name}")
print(f"Add 5 + 3: {calc.add(5, 3)}")
print(f"Pi value: {Calculator.get_pi()}")
print(f"Multiply 4 * 7: {Calculator.multiply(4, 7)}")

# Create object using class method
default_calc = Calculator.create_default()
print(f"Default calculator: {default_calc.name}")

print("\n=== Class Variables vs Instance Variables ===")

class Counter:
    # Class variable
    total_count = 0
    
    def __init__(self, name):
        # Instance variable
        self.name = name
        self.count = 0
        Counter.total_count += 1
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count
    
    @classmethod
    def get_total_count(cls):
        return cls.total_count

counter1 = Counter("Counter 1")
counter2 = Counter("Counter 2")

counter1.increment()
counter1.increment()
counter2.increment()

print(f"Counter 1 count: {counter1.get_count()}")
print(f"Counter 2 count: {counter2.get_count()}")
print(f"Total counters created: {Counter.get_total_count()}")

print("\n=== Special Methods (Dunder Methods) ===")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Developer representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length (number of pages)
    def __len__(self):
        return self.pages
    
    # Equality comparison
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("Python Guide", "John Doe", 300)
book2 = Book("Python Guide", "John Doe", 250)

print(f"Book: {book1}")
print(f"Book representation: {repr(book1)}")
print(f"Book length: {len(book1)} pages")
print(f"Books are equal: {book1 == book2}")

