# Error Handling in Python

print("=== Basic Try/Except ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    number = int("not a number")
except ValueError:
    print("Invalid number format!")

print("\n=== Handling Multiple Exceptions ===")

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid operand types")
        return None

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / 'a' = {divide(10, 'a')}")

print("\n=== Try/Except/Else/Finally ===")

def process_file(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
    else:
        # Executes if no exception occurred
        print(f"Successfully opened {filename}")
        content = file.read()
        file.close()
        return content
    finally:
        # Always executes
        print("File processing attempt completed")

# This will fail (file doesn't exist)
process_file("nonexistent.txt")

print("\n=== Catching All Exceptions ===")

def risky_operation():
    try:
        # Some operation that might fail
        result = 10 / 0
        return result
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {e}")
        return None

risky_operation()

print("\n=== Custom Exception Classes ===")

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds. Balance: ${balance}, Required: ${amount}"
        super().__init__(message)

class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValidationError("Initial balance cannot be negative")
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Test custom exceptions
try:
    account = BankAccount(100)
    print(f"Account created with balance: ${account.balance}")
    
    account.withdraw(50)
    print(f"After withdrawal: ${account.balance}")
    
    account.withdraw(100)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Error: {e}")
except ValidationError as e:
    print(f"Validation error: {e}")

print("\n=== Exception Hierarchy ===")

try:
    result = 10 / 0
except ArithmeticError:
    print("Caught ArithmeticError (parent of ZeroDivisionError)")
except ZeroDivisionError:
    print("This won't be reached")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError (more specific)")
except ArithmeticError:
    print("This won't be reached")

print("\n=== Raising Exceptions ===")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    if age < 18:
        raise ValueError("Must be 18 or older")
    return True

try:
    check_age(25)
    print("Age validated successfully")
except ValueError as e:
    print(f"Validation failed: {e}")

try:
    check_age(15)
except ValueError as e:
    print(f"Validation failed: {e}")

print("\n=== Exception Chaining ===")

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError as e:
        raise TypeError(f"Invalid data type: {data}") from e

try:
    result = process_data("not a number")
except TypeError as e:
    print(f"TypeError: {e}")
    print(f"Caused by: {e.__cause__}")

print("\n=== Assertions ===")

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {avg}")
    
    # This will raise AssertionError
    # avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")

print("\n=== Context Manager for Error Handling ===")

class ErrorLogger:
    """Context manager that logs errors"""
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Error logged: {exc_type.__name__}: {exc_val}")
        return True  # Suppress the exception for demonstration

with ErrorLogger():
    result = 10 / 2
    print(f"Result: {result}")

with ErrorLogger():
    result = 10 / 0  # This will be logged

print("\n=== Retry Pattern with Error Handling ===")

def retry_operation(max_attempts=3):
    """Decorator that retries operation on failure"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts:
                        print(f"Attempt {attempt} failed: {e}. Retrying...")
                    else:
                        print(f"All {max_attempts} attempts failed")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_attempts=3)
def unreliable_operation():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise RuntimeError("Operation failed")
    return "Success"

# This might succeed or fail after retries
try:
    result = unreliable_operation()
    print(f"Operation result: {result}")
except RuntimeError as e:
    print(f"Operation failed after retries: {e}")

