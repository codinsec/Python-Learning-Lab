# Authentication: JWT and OAuth2

## Overview
This topic covers authentication in FastAPI using JWT (JSON Web Tokens) and OAuth2. Learn how to implement secure authentication, handle user sessions, and work with OAuth2 flows.

## Learning Objectives
- Understand JWT tokens
- Implement JWT-based authentication
- Use OAuth2 with FastAPI
- Handle password hashing
- Create login and registration endpoints
- Protect routes with authentication
- Understand token expiration and refresh

## Topics Covered
- JWT token creation and validation
- Password hashing (bcrypt)
- OAuth2 password flow
- Authentication dependencies
- Protected routes
- Token refresh mechanism
- Security best practices

## How to Run
```bash
# Install dependencies
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart

# Run the application
uvicorn main:app --reload
```

## Examples
The `main.py` file contains practical examples demonstrating:
- JWT token generation
- Password hashing
- OAuth2 password flow
- Protected routes
- Token validation

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

