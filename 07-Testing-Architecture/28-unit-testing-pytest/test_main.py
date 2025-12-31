# Unit Tests with Pytest

import pytest
from main import add, subtract, multiply, divide, is_even, get_user_age, Calculator

print("=== Pytest Unit Testing Examples ===")
print("To run: pytest test_main.py -v")

print("\n=== Basic Test Functions ===")

def test_add():
    """Test addition function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction function"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Test multiplication function"""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

print("""
Basic test functions:
  - test_add()
  - test_subtract()
  - test_multiply()
""")

print("\n=== Exception Testing ===")

def test_divide_by_zero():
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_normal():
    """Test normal division"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

print("""
Exception testing:
  - test_divide_by_zero() - Tests exception is raised
  - test_divide_normal() - Tests normal operation
""")

print("\n=== Test Fixtures ===")

@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance"""
    calc = Calculator()
    yield calc
    calc.clear_history()

def test_calculator_add(calculator):
    """Test calculator using fixture"""
    result = calculator.add(5, 3)
    assert result == 8
    assert len(calculator.get_history()) == 1

def test_calculator_history(calculator):
    """Test calculator history"""
    calculator.add(2, 2)
    calculator.add(3, 3)
    history = calculator.get_history()
    assert len(history) == 2
    assert "2 + 2 = 4" in history

print("""
Fixtures:
  - @pytest.fixture - Creates reusable test setup
  - calculator fixture - Provides Calculator instance
""")

print("\n=== Parametrized Tests ===")

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    """Test add function with multiple inputs"""
    assert add(a, b) == expected

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (0, True),
    (100, True),
    (101, False)
])
def test_is_even_parametrized(n, expected):
    """Test is_even with multiple inputs"""
    assert is_even(n) == expected

print("""
Parametrized tests:
  - @pytest.mark.parametrize - Run test with multiple inputs
  - test_add_parametrized() - Tests multiple addition cases
  - test_is_even_parametrized() - Tests multiple even/odd cases
""")

print("\n=== Test Classes ===")

class TestCalculator:
    """Test class for Calculator"""
    
    @pytest.fixture
    def calc(self):
        """Fixture for test class"""
        return Calculator()
    
    def test_add(self, calc):
        """Test calculator add method"""
        assert calc.add(5, 3) == 8
    
    def test_history(self, calc):
        """Test calculator history"""
        calc.add(1, 1)
        assert len(calc.get_history()) == 1
    
    def test_clear_history(self, calc):
        """Test clearing history"""
        calc.add(1, 1)
        calc.clear_history()
        assert len(calc.get_history()) == 0

print("""
Test classes:
  - Organize related tests
  - Share fixtures within class
  - TestCalculator class example
""")

print("\n=== Testing with Dictionaries ===")

def test_get_user_age():
    """Test getting user age"""
    user = {"name": "Alice", "age": 30}
    assert get_user_age(user) == 30
    
    user_no_age = {"name": "Bob"}
    assert get_user_age(user_no_age) == 0

print("\n=== Assertion Messages ===")

def test_with_message():
    """Test with custom assertion message"""
    result = add(2, 2)
    assert result == 4, f"Expected 4, got {result}"

print("\n=== Running Tests ===")
print("""
To run these tests:

1. Install pytest:
   pip install pytest

2. Run all tests:
   pytest test_main.py

3. Run with verbose output:
   pytest test_main.py -v

4. Run specific test:
   pytest test_main.py::test_add

5. Run with coverage:
   pytest --cov=main test_main.py
""")

if __name__ == "__main__":
    print("\nNote: This file contains test examples.")
    print("Run with: pytest test_main.py -v")

