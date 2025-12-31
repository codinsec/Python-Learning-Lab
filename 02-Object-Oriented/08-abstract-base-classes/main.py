# Abstract Base Classes (ABC) in Python

from abc import ABC, abstractmethod

print("=== Basic Abstract Base Class ===")

class Shape(ABC):
    # Abstract method - must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # Regular method - can be used by all subclasses
    def describe(self):
        return f"This is a {self.__class__.__name__}"

# Cannot instantiate abstract class
# shape = Shape()  # This would raise TypeError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle: {rectangle.describe()}")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

print(f"\nCircle: {circle.describe()}")
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")

print("\n=== Abstract Properties ===")

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    @property
    def sound(self):
        return "Woof"
    
    def move(self):
        return "Running on four legs"

class Bird(Animal):
    @property
    def sound(self):
        return "Tweet"
    
    def move(self):
        return "Flying through the air"

dog = Dog()
bird = Bird()

print(f"Dog sound: {dog.sound}, movement: {dog.move()}")
print(f"Bird sound: {bird.sound}, movement: {bird.move()}")

print("\n=== Abstract Class with Concrete Methods ===")

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    # Concrete method - shared by all subclasses
    def log_query(self, query):
        print(f"Executing query: {query}")

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL database"
    
    def disconnect(self):
        return "Disconnected from MySQL database"
    
    def execute_query(self, query):
        self.log_query(query)
        return f"MySQL: {query} executed"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL database"
    
    def disconnect(self):
        return "Disconnected from PostgreSQL database"
    
    def execute_query(self, query):
        self.log_query(query)
        return f"PostgreSQL: {query} executed"

mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

print(mysql_db.connect())
print(mysql_db.execute_query("SELECT * FROM users"))
print(mysql_db.disconnect())

print(f"\n{postgres_db.connect()}")
print(postgres_db.execute_query("SELECT * FROM products"))
print(postgres_db.disconnect())

print("\n=== Multiple Abstract Methods ===")

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        pass
    
    @abstractmethod
    def get_balance(self):
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 1000.0
    
    def process_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Payment of ${amount} processed with credit card"
        return "Insufficient balance"
    
    def refund(self, transaction_id):
        return f"Refund processed for transaction {transaction_id}"
    
    def get_balance(self):
        return self.balance

processor = CreditCardProcessor("1234-5678-9012-3456")
print(f"Initial balance: ${processor.get_balance()}")
print(processor.process_payment(150.50))
print(f"Balance after payment: ${processor.get_balance()}")

