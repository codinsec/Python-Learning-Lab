# Conditionals and Loops in Python

print("=== Conditional Statements ===")

# Basic if/elif/else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")

# Match-case statement (Python 3.10+)
print("\n=== Match-Case Statement ===")

def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Unknown"

print(f"Monday: {get_day_type('Monday')}")
print(f"Saturday: {get_day_type('Saturday')}")

# For loops
print("\n=== For Loops ===")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Using range
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i)

# For loop with index
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loops
print("\n=== While Loops ===")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Loop control: break and continue
print("\n=== Loop Control ===")
print("Numbers 1-10, skip 5:")
for num in range(1, 11):
    if num == 5:
        continue
    if num > 8:
        break
    print(num)

# For-else clause (executes if loop completes without break)
print("\n=== For-Else ===")
numbers = [2, 4, 6, 8]
for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    print("All numbers are even")

# Nested loops
print("\n=== Nested Loops ===")
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  ")
    print()

