# Encapsulation and Properties in Python

print("=== Name Mangling (Private Attributes) ===")

class BankAccount:
    def __init__(self, account_number, balance):
        # Public attribute
        self.account_number = account_number
        # Private attribute (name mangling with __)
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"

account = BankAccount("12345", 1000)
print(f"Account number: {account.account_number}")
print(f"Balance: ${account.get_balance()}")

# Cannot access __balance directly
# print(account.__balance)  # AttributeError

# But can access with name mangling (not recommended)
print(f"Balance (via mangling): ${account._BankAccount__balance}")

print(account.deposit(500))
print(account.withdraw(200))

print("\n=== Protected Attributes (Convention) ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        # Protected attribute (convention with _)
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative")

person = Person("Alice", 25)
print(f"Name: {person.name}")
print(f"Age: {person.get_age()}")

# Can access _age directly (but convention says don't)
print(f"Age (direct): {person._age}")

person.set_age(26)
print(f"Updated age: {person.get_age()}")

print("\n=== Property Decorator ===")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Updated Celsius: {temp.celsius}°C")
print(f"Updated Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"Set to 86°F, Celsius is now: {temp.celsius}°C")

print("\n=== Property with Validation ===")

class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self._grade = None
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if value not in ['A', 'B', 'C', 'D', 'F', None]:
            raise ValueError("Grade must be A, B, C, D, F, or None")
        self._grade = value

student = Student("Bob", 20)
print(f"Student: {student.name}, Age: {student.age}")

student.age = 21
print(f"Updated age: {student.age}")

student.grade = 'A'
print(f"Grade: {student.grade}")

# This would raise ValueError
# student.age = 200

print("\n=== Computed Properties ===")

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    # Computed property (read-only)
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

rect = Rectangle(5, 3)
print(f"Rectangle: {rect.width} x {rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

rect.width = 7
print(f"\nUpdated width to 7")
print(f"New area: {rect.area}")
print(f"New perimeter: {rect.perimeter}")

print("\n=== Property Deleter ===")

class Config:
    def __init__(self):
        self._api_key = None
    
    @property
    def api_key(self):
        if self._api_key is None:
            return "No API key set"
        return f"API key: {self._api_key[:4]}****"
    
    @api_key.setter
    def api_key(self, value):
        if len(value) < 8:
            raise ValueError("API key must be at least 8 characters")
        self._api_key = value
    
    @api_key.deleter
    def api_key(self):
        print("API key deleted")
        self._api_key = None

config = Config()
print(config.api_key)

config.api_key = "secret_key_12345"
print(config.api_key)

del config.api_key
print(config.api_key)

