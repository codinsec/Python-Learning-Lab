# Pydantic Models in Python

from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import datetime

print("=== Basic Pydantic Model ===")

class User(BaseModel):
    name: str
    email: str
    age: int

# Create instance
user = User(name="Alice", email="alice@example.com", age=30)
print(f"User: {user}")
print(f"User name: {user.name}")
print(f"User dict: {user.dict()}")

print("\n=== Field Validation ===")

class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="Price must be positive")
    quantity: int = Field(default=0, ge=0)

# Valid product
product = Product(name="Laptop", price=999.99, quantity=5)
print(f"Product: {product}")

# Invalid product (will raise ValidationError)
try:
    invalid_product = Product(name="", price=-10, quantity=-1)
except Exception as e:
    print(f"Validation error caught: {type(e).__name__}")

print("\n=== Custom Validators ===")

class UserWithValidation(BaseModel):
    name: str
    email: str
    age: int
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('Age must be between 0 and 150')
        return v
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Email must contain @')
        return v

# Valid user
valid_user = UserWithValidation(name="Bob", email="bob@example.com", age=25)
print(f"Valid user: {valid_user}")

# Invalid user
try:
    invalid_user = UserWithValidation(name="Charlie", email="invalid", age=200)
except Exception as e:
    print(f"Validation error: {e}")

print("\n=== Optional Fields ===")

class OptionalUser(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    phone: Optional[str] = None

user1 = OptionalUser(name="Diana", email="diana@example.com")
user2 = OptionalUser(name="Eve", email="eve@example.com", age=28, phone="123-456-7890")

print(f"User without optional fields: {user1}")
print(f"User with optional fields: {user2}")

print("\n=== Default Values ===")

class UserWithDefaults(BaseModel):
    name: str
    email: str
    age: int = 18
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

user = UserWithDefaults(name="Frank", email="frank@example.com")
print(f"User with defaults: {user}")

print("\n=== Serialization ===")

class SerializeUser(BaseModel):
    name: str
    email: str
    age: int

user = SerializeUser(name="Grace", email="grace@example.com", age=32)

# To dictionary
user_dict = user.dict()
print(f"User as dict: {user_dict}")

# To JSON string
import json
user_json = user.json()
print(f"User as JSON: {user_json}")

# Parse JSON
parsed_user = SerializeUser.parse_raw(user_json)
print(f"Parsed from JSON: {parsed_user}")

print("\n=== Deserialization ===")

# From dictionary
user_data = {"name": "Henry", "email": "henry@example.com", "age": 40}
user = SerializeUser(**user_data)
print(f"User from dict: {user}")

# From JSON string
json_data = '{"name": "Iris", "email": "iris@example.com", "age": 35}'
user = SerializeUser.parse_raw(json_data)
print(f"User from JSON: {user}")

print("\n=== Nested Models ===")

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    name: str
    email: str
    address: Address

address = Address(street="123 Main St", city="Istanbul", zip_code="34000")
user = UserWithAddress(name="Jack", email="jack@example.com", address=address)

print(f"User with address: {user}")
print(f"User address city: {user.address.city}")

# From nested dict
user_data = {
    "name": "Kate",
    "email": "kate@example.com",
    "address": {
        "street": "456 Oak Ave",
        "city": "Ankara",
        "zip_code": "06000"
    }
}
user = UserWithAddress(**user_data)
print(f"User from nested dict: {user}")

print("\n=== Lists and Collections ===")

class UserWithTags(BaseModel):
    name: str
    email: str
    tags: List[str] = []

user = UserWithTags(
    name="Liam",
    email="liam@example.com",
    tags=["developer", "python", "backend"]
)
print(f"User with tags: {user}")

print("\n=== Model Configuration ===")

class ConfigUser(BaseModel):
    name: str
    email: str
    
    class Config:
        # Allow extra fields
        extra = "forbid"  # or "allow" or "ignore"
        
        # Example JSON schema
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com"
            }
        }

user = ConfigUser(name="Mia", email="mia@example.com")
print(f"Config user: {user}")

print("\n=== Field Aliases ===")

class AliasedUser(BaseModel):
    name: str = Field(..., alias="full_name")
    email: str = Field(..., alias="email_address")
    age: int
    
    class Config:
        allow_population_by_field_name = True

# Create with aliases
user = AliasedUser(full_name="Noah", email_address="noah@example.com", age=27)
print(f"User with aliases: {user}")

# Can also use field names
user2 = AliasedUser(name="Olivia", email="olivia@example.com", age=29)
print(f"User with field names: {user2}")

print("\n=== Validation Errors ===")

class StrictUser(BaseModel):
    name: str = Field(..., min_length=2)
    email: str
    age: int = Field(..., ge=0, le=120)

try:
    invalid = StrictUser(name="A", email="invalid-email", age=150)
except Exception as e:
    print(f"Validation errors: {e}")

print("\n=== Model Methods ===")

class UserWithMethods(BaseModel):
    name: str
    email: str
    age: int
    
    def get_display_name(self):
        return f"{self.name} ({self.age})"
    
    def is_adult(self):
        return self.age >= 18

user = UserWithMethods(name="Paul", email="paul@example.com", age=25)
print(f"Display name: {user.get_display_name()}")
print(f"Is adult: {user.is_adult()}")

print("\n=== Copy and Update ===")

user1 = SerializeUser(name="Quinn", email="quinn@example.com", age=30)

# Create copy
user2 = user1.copy()
print(f"Copied user: {user2}")

# Create copy with updates
user3 = user1.copy(update={"age": 31})
print(f"Updated copy: {user3}")

print("\n=== Model Inheritance ===")

class BaseUser(BaseModel):
    name: str
    email: str

class AdminUser(BaseUser):
    role: str = "admin"
    permissions: List[str] = ["read", "write", "delete"]

admin = AdminUser(name="Rachel", email="rachel@example.com", permissions=["read", "write"])
print(f"Admin user: {admin}")

print("\n=== JSON Schema ===")

schema = SerializeUser.schema()
print("User model JSON schema:")
print(f"  Properties: {list(schema['properties'].keys())}")
print(f"  Required: {schema.get('required', [])}")

print("\n=== Best Practices ===")

best_practices = [
    "Use Pydantic models for data validation",
    "Define clear field types and constraints",
    "Use validators for complex validation logic",
    "Keep models focused and single-purpose",
    "Use nested models for complex structures",
    "Handle validation errors gracefully",
    "Use Field() for additional constraints",
    "Document models with descriptions"
]

print("Pydantic best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Integration with FastAPI ===")

print("""
Pydantic models work seamlessly with FastAPI:

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: UserCreate):
    # FastAPI automatically validates request body
    return {"message": f"User {user.name} created"}
""")

