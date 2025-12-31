# Inheritance and Mixins in Python

print("=== Single Inheritance ===")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"
    
    def climb(self):
        return f"{self.name} is climbing a tree"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())
print(dog.make_sound())
print(dog.fetch())

print(f"\n{cat.info()}")
print(cat.make_sound())
print(cat.climb())

print("\n=== Multiple Inheritance ===")

class Flyable:
    def fly(self):
        return "Flying through the air"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack! Quack!"

duck = Duck("Donald")
print(duck.info())
print(duck.make_sound())
print(duck.fly())
print(duck.swim())

print("\n=== Method Resolution Order (MRO) ===")

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"D's method: {d.method()}")
print(f"Method Resolution Order: {D.__mro__}")

print("\n=== Using super() with Multiple Inheritance ===")

class Base1:
    def __init__(self):
        print("Base1 initialized")

class Base2:
    def __init__(self):
        print("Base2 initialized")

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()
        print("Derived initialized")

derived = Derived()

print("\n=== Mixins Pattern ===")

# Mixin classes provide reusable functionality
class JSONSerializableMixin:
    def to_json(self):
        import json
        from datetime import datetime
        # Convert datetime objects to strings for JSON serialization
        data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return json.dumps(data)

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        from datetime import datetime
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class User(TimestampMixin, JSONSerializableMixin):
    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email

user = User("alice", "alice@example.com")
print(f"User created at: {user.created_at}")
print(f"User as JSON: {user.to_json()}")

print("\n=== Type Checking ===")

# isinstance() - check if object is instance of class
print(f"dog is Animal: {isinstance(dog, Animal)}")
print(f"dog is Dog: {isinstance(dog, Dog)}")
print(f"dog is Cat: {isinstance(dog, Cat)}")

# issubclass() - check if class is subclass of another
print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
print(f"Cat is subclass of Animal: {issubclass(Cat, Animal)}")
print(f"Dog is subclass of Cat: {issubclass(Dog, Cat)}")

print("\n=== Extending Parent Methods ===")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def start(self):
        # Extend parent method
        parent_message = super().start()
        return f"{parent_message} (electric mode, {self.battery_capacity}kWh battery)"

car = ElectricCar("Tesla", "Model 3", 75)
print(car.start())

