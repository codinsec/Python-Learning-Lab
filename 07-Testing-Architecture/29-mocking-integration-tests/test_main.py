# Mocking and Integration Tests

import pytest
from unittest.mock import Mock, patch, MagicMock
from main import fetch_user_data, process_payment, send_email, Database, UserService

print("=== Mocking and Integration Tests ===")
print("To run: pytest test_main.py -v")

print("\n=== Basic Mocking ===")

def test_basic_mock():
    """Test basic mock object"""
    mock_obj = Mock()
    mock_obj.method.return_value = "mocked result"
    
    assert mock_obj.method() == "mocked result"
    mock_obj.method.assert_called_once()

print("""
Basic mocking:
  - Mock() - Create mock object
  - return_value - Set return value
  - assert_called_once() - Verify method was called
""")

print("\n=== Mocking Functions ===")

@patch('main.requests.get')
def test_fetch_user_data(mock_get):
    """Test fetch_user_data with mocked requests"""
    # Setup mock response
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "name": "Alice"}
    mock_get.return_value = mock_response
    
    # Test function
    result = fetch_user_data(1)
    
    # Assertions
    assert result == {"id": 1, "name": "Alice"}
    mock_get.assert_called_once_with("https://api.example.com/users/1")

print("""
Mocking functions:
  - @patch decorator - Mock function during test
  - test_fetch_user_data() - Mocks requests.get
""")

print("\n=== Mocking with Return Values ===")

@patch('main.time.sleep')
@patch('main.process_payment')
def test_process_payment_mock(mock_payment, mock_sleep):
    """Test process_payment with mocked time"""
    mock_payment.return_value = {"status": "success", "transaction_id": "99999"}
    
    result = process_payment(100, "1234-5678")
    
    assert result["status"] == "success"
    mock_sleep.assert_called_once()

print("""
Mocking with return values:
  - mock.return_value - Set return value
  - Multiple @patch decorators - Mock multiple dependencies
""")

print("\n=== Mocking with Side Effects ===")

def test_mock_side_effect():
    """Test mock with side effect"""
    mock_func = Mock()
    mock_func.side_effect = [1, 2, 3]
    
    assert mock_func() == 1
    assert mock_func() == 2
    assert mock_func() == 3

def test_mock_side_effect_exception():
    """Test mock that raises exception"""
    mock_func = Mock()
    mock_func.side_effect = ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        mock_func()

print("""
Side effects:
  - side_effect - Can return different values or raise exceptions
  - Useful for testing error handling
""")

print("\n=== Context Manager Patching ===")

def test_patch_context_manager():
    """Test using patch as context manager"""
    with patch('main.send_email') as mock_email:
        mock_email.return_value = True
        
        result = send_email("test@example.com", "Test", "Body")
        
        assert result is True
        mock_email.assert_called_once()

print("""
Context manager patching:
  - with patch() - Temporary mock within context
  - Useful when you don't want to use decorator
""")

print("\n=== Mocking Classes ===")

@patch('main.Database')
def test_user_service_with_mock_db(mock_db_class):
    """Test UserService with mocked Database"""
    # Setup mock database instance
    mock_db_instance = Mock()
    mock_db_instance.save.return_value = True
    mock_db_instance.get.return_value = {"username": "test", "email": "test@example.com"}
    mock_db_class.return_value = mock_db_instance
    
    # Create service with mocked database
    service = UserService(mock_db_instance)
    user = service.create_user("test", "test@example.com")
    
    assert user["username"] == "test"
    mock_db_instance.save.assert_called_once()

print("""
Mocking classes:
  - Mock entire class
  - Mock class instances
  - Test code that depends on classes
""")

print("\n=== Integration Tests ===")

def test_user_service_integration():
    """Integration test with real Database"""
    # Use real Database (not mocked)
    db = Database()
    service = UserService(db)
    
    # Create user
    user = service.create_user("alice", "alice@example.com")
    assert user["username"] == "alice"
    
    # Retrieve user
    retrieved = service.get_user("alice")
    assert retrieved["username"] == "alice"
    assert retrieved["email"] == "alice@example.com"

print("""
Integration tests:
  - Use real dependencies
  - Test multiple components together
  - Verify system works as a whole
""")

print("\n=== MagicMock ===")

def test_magic_mock():
    """Test using MagicMock"""
    mock_obj = MagicMock()
    mock_obj.attribute = "value"
    mock_obj.method.return_value = "result"
    
    assert mock_obj.attribute == "value"
    assert mock_obj.method() == "result"
    assert len(mock_obj) == 0  # MagicMock supports len()

print("""
MagicMock:
  - Supports magic methods automatically
  - More flexible than Mock
  - Useful for complex objects
""")

print("\n=== Verifying Mock Calls ===")

def test_verify_calls():
    """Test verifying mock was called correctly"""
    mock_func = Mock()
    mock_func("arg1", "arg2", keyword="value")
    
    # Verify calls
    mock_func.assert_called_once()
    mock_func.assert_called_with("arg1", "arg2", keyword="value")
    assert mock_func.call_count == 1

print("""
Verifying calls:
  - assert_called_once() - Called exactly once
  - assert_called_with() - Called with specific arguments
  - call_count - Number of times called
""")

print("\n=== Patching Multiple Targets ===")

@patch('main.send_email')
@patch('main.process_payment')
def test_multiple_mocks(mock_payment, mock_email):
    """Test with multiple mocked functions"""
    mock_payment.return_value = {"status": "success"}
    mock_email.return_value = True
    
    payment_result = process_payment(100, "1234")
    email_result = send_email("test@example.com", "Test", "Body")
    
    assert payment_result["status"] == "success"
    assert email_result is True

print("""
Multiple mocks:
  - Stack @patch decorators
  - Mocks are passed as arguments in reverse order
""")

print("\n=== Best Practices ===")

best_practices = [
    "Mock external dependencies (APIs, databases, file systems)",
    "Don't mock code you're testing",
    "Use integration tests for critical paths",
    "Keep mocks simple and focused",
    "Verify mock calls when important",
    "Use real objects in integration tests",
    "Mock at the right level (not too deep, not too shallow)"
]

print("Mocking best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Running Tests ===")
print("""
To run these tests:

1. Install dependencies:
   pip install pytest pytest-mock

2. Run tests:
   pytest test_main.py -v

3. Run with coverage:
   pytest --cov=main test_main.py
""")

if __name__ == "__main__":
    print("\nNote: This file contains test examples.")
    print("Run with: pytest test_main.py -v")

