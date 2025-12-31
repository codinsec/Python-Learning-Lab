# SOLID Principles - Pythonic Examples

print("=== SOLID Principles in Python ===\n")

print("=== 1. Single Responsibility Principle (SRP) ===")
print("A class should have only one reason to change")

# Violation: Class does too much
class UserManager:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        print(f"Saving {self.name} to database")
    
    def send_email(self):
        print(f"Sending email to {self.email}")
    
    def validate_email(self):
        return "@" in self.email

print("""
Violation Example:
  UserManager handles user data, database, email, and validation
  Multiple responsibilities = multiple reasons to change
""")

# Following SRP: Separate concerns
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send(self, user):
        print(f"Sending email to {user.email}")

class UserValidator:
    def validate_email(self, email):
        return "@" in email

print("""
Following SRP:
  User - Data only
  UserRepository - Database operations
  EmailService - Email operations
  UserValidator - Validation logic
  Each class has single responsibility
""")

print("\n=== 2. Open/Closed Principle (OCP) ===")
print("Open for extension, closed for modification")

# Violation: Modifying existing code to add features
class AreaCalculator:
    def calculate(self, shape_type, *args):
        if shape_type == "circle":
            return 3.14159 * args[0] ** 2
        elif shape_type == "rectangle":
            return args[0] * args[1]
        # Adding new shape requires modifying this method

print("""
Violation Example:
  Adding new shapes requires modifying AreaCalculator
  Violates OCP - should be open for extension, closed for modification
""")

# Following OCP: Use abstraction
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate(self, shape):
        return shape.area()

# Adding new shape doesn't require modifying AreaCalculator
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

print("""
Following OCP:
  New shapes can be added without modifying AreaCalculator
  Extend through inheritance, not modification
""")

print("\n=== 3. Liskov Substitution Principle (LSP) ===")
print("Subtypes must be substitutable for their base types")

# Violation: Subclass changes expected behavior
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

def make_bird_fly(bird):
    bird.fly()  # This will fail for Penguin

print("""
Violation Example:
  Penguin breaks LSP - can't be used where Bird is expected
  make_bird_fly() will fail for Penguin
""")

# Following LSP: Proper inheritance hierarchy
class Bird:
    def move(self):
        return "Moving"

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"

def make_bird_move(bird):
    return bird.move()  # Works for all Bird subclasses

print("""
Following LSP:
  All Bird subclasses can be used interchangeably
  Penguin doesn't break expected behavior
""")

print("\n=== 4. Interface Segregation Principle (ISP) ===")
print("Clients should not depend on interfaces they don't use")

# Violation: Fat interface
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass

class Human(Worker):
    def work(self):
        return "Human working"
    
    def eat(self):
        return "Human eating"
    
    def sleep(self):
        return "Human sleeping"

class Robot(Worker):
    def work(self):
        return "Robot working"
    
    def eat(self):
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self):
        raise NotImplementedError("Robots don't sleep")

print("""
Violation Example:
  Robot forced to implement eat() and sleep()
  Violates ISP - Robot doesn't need these methods
""")

# Following ISP: Segregated interfaces
class Workable:
    def work(self):
        raise NotImplementedError

class Eatable:
    def eat(self):
        raise NotImplementedError

class Sleepable:
    def sleep(self):
        raise NotImplementedError

class Human(Workable, Eatable, Sleepable):
    def work(self):
        return "Human working"
    
    def eat(self):
        return "Human eating"
    
    def sleep(self):
        return "Human sleeping"

class Robot(Workable):
    def work(self):
        return "Robot working"

print("""
Following ISP:
  Interfaces are segregated
  Robot only implements what it needs
  No forced implementation of unused methods
""")

print("\n=== 5. Dependency Inversion Principle (DIP) ===")
print("Depend on abstractions, not concretions")

# Violation: High-level module depends on low-level module
class MySQLDatabase:
    def save(self, data):
        print(f"Saving to MySQL: {data}")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Direct dependency on concrete class
    
    def save_user(self, user):
        self.db.save(user)

print("""
Violation Example:
  UserService directly depends on MySQLDatabase
  Hard to change database implementation
  Violates DIP
""")

# Following DIP: Depend on abstraction
class Database:
    def save(self, data):
        raise NotImplementedError

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving to MySQL: {data}")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving to PostgreSQL: {data}")

class UserService:
    def __init__(self, database):
        self.db = database  # Depends on abstraction
    
    def save_user(self, user):
        self.db.save(user)

print("""
Following DIP:
  UserService depends on Database abstraction
  Can easily swap database implementations
  Follows dependency inversion
""")

print("\n=== Pythonic SOLID Examples ===")

# Using ABC for interfaces
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} with credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} with PayPal"

class PaymentService:
    def __init__(self, processor):
        self.processor = processor
    
    def pay(self, amount):
        return self.processor.process_payment(amount)

print("""
Pythonic implementation:
  - Uses ABC for abstract base classes
  - Dependency injection in PaymentService
  - Easy to extend with new processors
  - Follows DIP and OCP
""")

print("\n=== Benefits of SOLID Principles ===")

benefits = [
    "Maintainability - Easier to understand and modify",
    "Testability - Easier to write unit tests",
    "Extensibility - Easy to add new features",
    "Reusability - Components can be reused",
    "Flexibility - Easy to swap implementations",
    "Reduced coupling - Components are loosely coupled"
]

print("Benefits:")
for i, benefit in enumerate(benefits, 1):
    print(f"  {i}. {benefit}")

print("\n=== When to Apply SOLID ===")

print("""
Apply SOLID when:
  - Building large, complex systems
  - Code needs to be maintained long-term
  - Multiple developers work on codebase
  - Requirements change frequently
  - Code needs to be tested thoroughly

Don't over-engineer:
  - Simple scripts don't need full SOLID
  - Prototypes can be less strict
  - Balance principles with practicality
""")

