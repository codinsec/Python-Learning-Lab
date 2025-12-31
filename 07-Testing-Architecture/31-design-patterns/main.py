# Design Patterns in Python

print("=== Design Patterns in Python ===\n")

print("=== 1. Singleton Pattern ===")
print("Ensure a class has only one instance")

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = {}
            self.initialized = True

# Test singleton
s1 = Singleton()
s2 = Singleton()
print(f"s1 is s2: {s1 is s2}")  # True - same instance

# Pythonic way using decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Config:
    def __init__(self):
        self.settings = {}

config1 = Config()
config2 = Config()
print(f"config1 is config2: {config1 is config2}")

print("""
Singleton Pattern:
  - Ensures only one instance exists
  - Useful for configuration, logging, database connections
  - Pythonic: Use decorator or __new__ method
""")

print("\n=== 2. Factory Pattern ===")
print("Create objects without specifying exact class")

class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Using factory
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")

# Pythonic factory using dictionary
class AnimalFactoryDict:
    _animals = {
        "dog": Dog,
        "cat": Cat
    }
    
    @classmethod
    def create(cls, animal_type):
        animal_class = cls._animals.get(animal_type)
        if animal_class:
            return animal_class()
        raise ValueError(f"Unknown animal type: {animal_type}")

print("""
Factory Pattern:
  - Centralizes object creation
  - Hides creation logic
  - Easy to add new types
""")

print("\n=== 3. Observer Pattern ===")
print("Define one-to-many dependency between objects")

class Observer:
    def update(self, message):
        raise NotImplementedError

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email
    
    def update(self, message):
        print(f"Email to {self.email}: {message}")

class SMSObserver(Observer):
    def __init__(self, phone):
        self.phone = phone
    
    def update(self, message):
        print(f"SMS to {self.phone}: {message}")

# Usage
newsletter = Subject()
email_obs = EmailObserver("alice@example.com")
sms_obs = SMSObserver("123-456-7890")

newsletter.attach(email_obs)
newsletter.attach(sms_obs)

newsletter.notify("New article published!")

print("""
Observer Pattern:
  - Subject notifies observers of changes
  - Loose coupling between subject and observers
  - Useful for event handling, notifications
""")

print("\n=== 4. Strategy Pattern ===")
print("Define family of algorithms, make them interchangeable")

class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with bank transfer"

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        return self.strategy.pay(amount)
    
    def set_strategy(self, strategy):
        self.strategy = strategy

# Usage
processor = PaymentProcessor(CreditCardPayment())
print(processor.process_payment(100))

processor.set_strategy(PayPalPayment())
print(processor.process_payment(200))

print("""
Strategy Pattern:
  - Encapsulates algorithms
  - Makes them interchangeable
  - Follows Open/Closed Principle
""")

print("\n=== 5. Decorator Pattern (Pythonic) ===")
print("Add behavior to objects dynamically")

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello, World!"

print(f"Decorated text: {get_text()}")

# Class-based decorator
class Logger:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} returned {result}")
        return result

@Logger
def add(a, b):
    return a + b

result = add(5, 3)

print("""
Decorator Pattern:
  - Python has built-in decorator support
  - Add functionality without modifying original
  - Function and class decorators
""")

print("\n=== 6. Builder Pattern ===")
print("Construct complex objects step by step")

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False
    
    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.bacon:
            toppings.append("bacon")
        return f"Pizza(size={self.size}, toppings={', '.join(toppings)})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_bacon(self):
        self.pizza.bacon = True
        return self
    
    def build(self):
        return self.pizza

# Usage
pizza = (PizzaBuilder()
         .set_size("large")
         .add_cheese()
         .add_pepperoni()
         .build())

print(f"Built pizza: {pizza}")

print("""
Builder Pattern:
  - Constructs complex objects step by step
  - Fluent interface for readability
  - Useful for objects with many optional parameters
""")

print("\n=== 7. Adapter Pattern ===")
print("Allow incompatible interfaces to work together")

class OldSystem:
    def old_method(self, data):
        return f"Old format: {data}"

class NewSystem:
    def new_method(self, data):
        return f"New format: {data}"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def new_method(self, data):
        # Adapt old system to new interface
        return self.old_system.old_method(data)

# Usage
old = OldSystem()
adapter = Adapter(old)
print(adapter.new_method("test"))

print("""
Adapter Pattern:
  - Makes incompatible interfaces work together
  - Wraps old system with new interface
  - Useful for integrating legacy code
""")

print("\n=== When to Use Design Patterns ===")

print("""
Use patterns when:
  - Solving recurring problems
  - Code needs to be flexible and extensible
  - Working with complex systems
  - Team needs common vocabulary

Don't overuse:
  - Simple problems don't need complex patterns
  - Patterns add abstraction - use when needed
  - Python's features often make patterns simpler
""")

print("\n=== Pythonic Pattern Implementation ===")

print("""
Python makes many patterns simpler:
  - Decorators: Built-in language feature
  - Factory: Can use functions or classes
  - Strategy: Functions are first-class objects
  - Observer: Can use events or callbacks
  - Singleton: __new__ method or decorator

Key: Use Python's features to implement patterns naturally
""")

