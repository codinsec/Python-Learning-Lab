# Code to be tested

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    """Check if number is even"""
    return n % 2 == 0

def get_user_age(user):
    """Get age from user dictionary"""
    return user.get("age", 0)

class Calculator:
    """Simple calculator class"""
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

