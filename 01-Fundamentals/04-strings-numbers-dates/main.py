# Strings, Numbers, and Dates in Python

import math
from datetime import datetime, timedelta, date

print("=== String Operations ===")

# String creation
text = "Hello, Python!"
print(f"Original: {text}")

# String methods
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Replace: {text.replace('Python', 'World')}")

# String slicing
print(f"First 5 chars: {text[:5]}")
print(f"Last 6 chars: {text[-6:]}")

# String splitting and joining
words = "apple,banana,cherry"
fruit_list = words.split(",")
print(f"Split: {fruit_list}")

joined = " | ".join(fruit_list)
print(f"Joined: {joined}")

# String formatting
print("\n=== String Formatting ===")

name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"
print(f"F-string: {message}")

# .format() method
message2 = "My name is {} and I'm {} years old".format(name, age)
print(f".format(): {message2}")

# Format with precision
pi = math.pi
print(f"Pi with 2 decimals: {pi:.2f}")
print(f"Number with padding: {42:05d}")

# String checking methods
print("\n=== String Checking ===")
email = "user@example.com"
print(f"Is digit: {'123'.isdigit()}")
print(f"Is alpha: {'Hello'.isalpha()}")
print(f"Starts with: {email.startswith('user')}")
print(f"Ends with: {email.endswith('.com')}")

# Numbers
print("\n=== Numeric Operations ===")

# Basic arithmetic
a, b = 10, 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Math module
print(f"\nSquare root of 16: {math.sqrt(16)}")
print(f"Power: 2^8 = {math.pow(2, 8)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Round 4.567 to 2 decimals: {round(4.567, 2)}")

# Dates and Times
print("\n=== Date and Time ===")

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Create specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")

# Date arithmetic
today = date.today()
age_days = (today - birthday).days
print(f"Days since birthday: {age_days}")

# Add/subtract time
future_date = now + timedelta(days=30, hours=5)
print(f"30 days and 5 hours from now: {future_date}")

# Date formatting
print("\n=== Date Formatting ===")
formats = [
    ("%Y-%m-%d", "ISO format"),
    ("%d/%m/%Y", "DD/MM/YYYY"),
    ("%B %d, %Y", "Month Day, Year"),
    ("%A, %B %d", "Day, Month Day")
]

for fmt, desc in formats:
    print(f"{desc}: {now.strftime(fmt)}")

# Parse date from string
date_string = "2024-01-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"\nParsed date: {parsed_date}")

# Date components
print(f"\nDate components:")
print(f"  Year: {now.year}")
print(f"  Month: {now.month}")
print(f"  Day: {now.day}")
print(f"  Hour: {now.hour}")
print(f"  Minute: {now.minute}")
print(f"  Weekday: {now.strftime('%A')}")

