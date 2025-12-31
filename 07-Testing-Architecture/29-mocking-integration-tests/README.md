# Mocking and Integration Tests

## Overview
This topic covers mocking in Python testing and integration testing. Learn how to mock external dependencies, test code in isolation, and write integration tests that verify multiple components work together.

## Learning Objectives
- Understand mocking and its use cases
- Use `unittest.mock` for mocking
- Mock functions, classes, and methods
- Use `patch` decorator and context manager
- Write integration tests
- Test API endpoints
- Mock external services

## Topics Covered
- Mock objects and patching
- Mocking functions and methods
- Mocking classes and instances
- Return values and side effects
- Integration testing
- Testing with real dependencies
- Best practices for mocking

## How to Run
```bash
# Install pytest and pytest-mock
pip install pytest pytest-mock

# Run tests
pytest test_main.py -v
```

## Examples
The `main.py` file contains code to test, and `test_main.py` contains examples demonstrating:
- Basic mocking
- Patching functions and classes
- Integration tests
- Testing with mocks

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

