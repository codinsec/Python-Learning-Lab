# Dataclasses and Enums in Python

from dataclasses import dataclass, field
from enum import Enum, IntEnum, Flag, auto

print("=== Basic Dataclass ===")

@dataclass
class Point:
    x: float
    y: float

point1 = Point(3.0, 4.0)
point2 = Point(3.0, 4.0)

print(f"Point1: {point1}")
print(f"Point2: {point2}")
print(f"Points are equal: {point1 == point2}")

# Dataclass automatically provides __init__, __repr__, __eq__

print("\n=== Dataclass with Default Values ===")

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"
    active: bool = True

person1 = Person("Alice", 25)
person2 = Person("Bob", 30, "bob@example.com", False)

print(f"Person1: {person1}")
print(f"Person2: {person2}")

print("\n=== Dataclass with Field Defaults ===")

@dataclass
class ShoppingCart:
    customer_name: str
    items: list = field(default_factory=list)
    total: float = 0.0
    
    def add_item(self, item_name, price):
        self.items.append(item_name)
        self.total += price

cart = ShoppingCart("Alice")
cart.add_item("Book", 15.99)
cart.add_item("Pen", 2.50)

print(f"Cart: {cart}")
print(f"Total: ${cart.total}")

print("\n=== Frozen Dataclass (Immutable) ===")

@dataclass(frozen=True)
class Configuration:
    host: str
    port: int
    debug: bool = False

config = Configuration("localhost", 8080, True)
print(f"Config: {config}")

# Cannot modify frozen dataclass
# config.port = 9000  # This would raise FrozenInstanceError

print("\n=== Dataclass with Methods ===")

@dataclass
class Rectangle:
    width: float
    height: float
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5.0, 3.0)
print(f"Rectangle: {rect}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

print("\n=== Basic Enum ===")

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

# Access enum members
print(f"Status.PENDING: {Status.PENDING}")
print(f"Status.PENDING.value: {Status.PENDING.value}")
print(f"Status.PENDING.name: {Status.PENDING.name}")

# Compare enum members
task_status = Status.IN_PROGRESS
print(f"Task status: {task_status}")
print(f"Is completed: {task_status == Status.COMPLETED}")
print(f"Is in progress: {task_status == Status.IN_PROGRESS}")

print("\n=== Enum Iteration ===")

print("All status values:")
for status in Status:
    print(f"  {status.name}: {status.value}")

print("\n=== IntEnum ===")

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# IntEnum can be compared with integers
priority = Priority.HIGH
print(f"Priority: {priority}")
print(f"Priority value: {priority.value}")
print(f"Is high priority: {priority >= Priority.MEDIUM}")
print(f"Can compare with int: {priority > 2}")

print("\n=== Enum with Auto Values ===")

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()

print("Color enum values:")
for color in Color:
    print(f"  {color.name}: {color.value}")

print("\n=== Flag Enum (Bitwise Operations) ===")

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()

# Combine permissions
read_write = Permission.READ | Permission.WRITE
all_permissions = Permission.READ | Permission.WRITE | Permission.EXECUTE | Permission.DELETE

print(f"Read-Write: {read_write}")
print(f"All permissions: {all_permissions}")

# Check permissions
user_permission = Permission.READ | Permission.WRITE
print(f"Can read: {Permission.READ in user_permission}")
print(f"Can execute: {Permission.EXECUTE in user_permission}")

print("\n=== Enum in Dataclass ===")

@dataclass
class Task:
    title: str
    status: Status
    priority: Priority
    
    def is_high_priority(self):
        return self.priority >= Priority.HIGH

task1 = Task("Fix bug", Status.IN_PROGRESS, Priority.HIGH)
task2 = Task("Write docs", Status.PENDING, Priority.LOW)

print(f"Task1: {task1.title}, Status: {task1.status.value}, Priority: {task1.priority.name}")
print(f"Task1 is high priority: {task1.is_high_priority()}")
print(f"Task2 is high priority: {task2.is_high_priority()}")

print("\n=== Enum with Custom Methods ===")

class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    
    def opposite(self):
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }
        return opposites[self]

current_direction = Direction.NORTH
print(f"Current direction: {current_direction.value}")
print(f"Opposite direction: {current_direction.opposite().value}")

