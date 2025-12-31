# FastAPI Basics and Routing

## Overview
This topic covers FastAPI fundamentals: creating APIs, defining routes, handling HTTP methods, path parameters, query parameters, and request/response models. FastAPI is a modern, fast web framework for building APIs with Python.

## Learning Objectives
- Create a FastAPI application
- Define routes and HTTP methods
- Use path parameters and query parameters
- Handle request bodies
- Define response models
- Understand FastAPI's automatic documentation
- Work with status codes and responses

## Topics Covered
- FastAPI installation and setup
- Creating FastAPI app instance
- Route decorators (@app.get, @app.post, etc.)
- Path parameters
- Query parameters
- Request bodies
- Response models
- Status codes
- Automatic API documentation (Swagger/OpenAPI)

## How to Run
```bash
# Install FastAPI and uvicorn
pip install fastapi uvicorn

# Run the application
uvicorn main:app --reload
```

Then visit:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Examples
The `main.py` file contains practical examples demonstrating:
- Basic FastAPI setup
- Different HTTP methods
- Path and query parameters
- Request/response handling
- Error responses

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

