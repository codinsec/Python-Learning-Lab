# Dependency Injection in FastAPI

## Overview
This topic covers FastAPI's powerful dependency injection system. Learn how to create reusable dependencies, share common logic across routes, and manage application state using dependency injection.

## Learning Objectives
- Understand dependency injection concepts
- Create function dependencies
- Use class-based dependencies
- Share dependencies across routes
- Create sub-dependencies
- Use dependencies for authentication
- Manage database connections with dependencies

## Topics Covered
- Function dependencies
- Class dependencies
- Dependency injection with `Depends()`
- Sub-dependencies
- Dependency scopes
- Common dependency patterns
- Database session dependencies

## How to Run
```bash
# Install FastAPI and uvicorn
pip install fastapi uvicorn

# Run the application
uvicorn main:app --reload
```

## Examples
The `main.py` file contains practical examples demonstrating:
- Basic dependency injection
- Function and class dependencies
- Sub-dependencies
- Common use cases (pagination, authentication, etc.)

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

