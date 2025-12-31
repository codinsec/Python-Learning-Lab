# Authentication: JWT and OAuth2 in FastAPI

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import hashlib

app = FastAPI(title="Authentication: JWT and OAuth2")

print("=== FastAPI Authentication: JWT and OAuth2 ===")
print("To run: uvicorn main:app --reload")
print("\nNote: This is a conceptual example. For production, use:")
print("  - python-jose for JWT")
print("  - passlib[bcrypt] for password hashing")

print("\n=== OAuth2 Password Flow Setup ===")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory user database (for demonstration)
fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": "hashed_password_123",  # In production, use bcrypt
        "email": "alice@example.com"
    },
    "bob": {
        "username": "bob",
        "hashed_password": "hashed_password_456",
        "email": "bob@example.com"
    }
}

# Secret key for JWT (in production, use environment variable)
SECRET_KEY = "your-secret-key-here-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

print("""
OAuth2 configuration:
  - Token URL: /token
  - Algorithm: HS256
  - Token expiration: 30 minutes
""")

print("\n=== Password Hashing (Conceptual) ===")

def hash_password(password: str) -> str:
    """Hash password (conceptual - use bcrypt in production)"""
    # In production: from passlib.context import CryptContext
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # return pwd_context.hash(password)
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password (conceptual - use bcrypt in production)"""
    # In production: return pwd_context.verify(plain_password, hashed_password)
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

print("""
Password hashing functions:
  - hash_password(): Hash a password
  - verify_password(): Verify password against hash
  - In production, use bcrypt via passlib
""")

print("\n=== JWT Token Functions (Conceptual) ===")

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create JWT access token (conceptual)"""
    # In production: from jose import jwt
    # to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.utcnow() + expires_delta
    # else:
    #     expire = datetime.utcnow() + timedelta(minutes=15)
    # to_encode.update({"exp": expire})
    # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # return encoded_jwt
    
    # Conceptual return
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    return f"fake_token_{data.get('sub')}_{expire.timestamp()}"

def verify_token(token: str):
    """Verify JWT token (conceptual)"""
    # In production: from jose import jwt, JWTError
    # try:
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #     return payload
    # except JWTError:
    #     return None
    
    # Conceptual verification
    if token.startswith("fake_token_"):
        return {"sub": "alice"}  # Mock payload
    return None

print("""
JWT token functions:
  - create_access_token(): Create JWT token
  - verify_token(): Verify and decode JWT token
  - In production, use python-jose library
""")

print("\n=== User Authentication Functions ===")

def get_user(username: str):
    """Get user from database"""
    if username in fake_users_db:
        return fake_users_db[username]
    return None

def authenticate_user(username: str, password: str):
    """Authenticate user"""
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """OAuth2 password flow login endpoint"""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

print("""
Login endpoint:
  POST /token
  Form data: username, password
  Returns: access_token, token_type
""")

print("\n=== Current User Dependency ===")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current authenticated user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = verify_token(token)
    if payload is None:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    
    return user

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    """Get current user information"""
    return {
        "username": current_user["username"],
        "email": current_user["email"]
    }

print("""
Protected endpoint:
  GET /users/me
  Requires: Authorization: Bearer <token>
""")

print("\n=== Protected Routes ===")

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    """Example protected route"""
    return {
        "message": "This is a protected route",
        "user": current_user["username"]
    }

@app.get("/items")
async def get_items(current_user: dict = Depends(get_current_user)):
    """Get items (protected)"""
    return {
        "items": ["item1", "item2", "item3"],
        "user": current_user["username"]
    }

print("""
Protected routes:
  GET /protected - Requires authentication
  GET /items - Requires authentication
""")

print("\n=== User Registration (Example) ===")

@app.post("/register")
async def register(username: str, password: str, email: str):
    """Register new user"""
    if username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    hashed_password = hash_password(password)
    fake_users_db[username] = {
        "username": username,
        "hashed_password": hashed_password,
        "email": email
    }
    
    return {"message": "User registered successfully", "username": username}

print("""
Registration endpoint:
  POST /register?username=test&password=test123&email=test@example.com
""")

print("\n=== Token Refresh (Conceptual) ===")

@app.post("/refresh")
async def refresh_token(current_user: dict = Depends(get_current_user)):
    """Refresh access token"""
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    new_token = create_access_token(
        data={"sub": current_user["username"]},
        expires_delta=access_token_expires
    )
    
    return {"access_token": new_token, "token_type": "bearer"}

print("""
Token refresh endpoint:
  POST /refresh
  Requires: Valid access token
  Returns: New access token
""")

print("\n=== OAuth2 Scopes (Conceptual) ===")

print("""
OAuth2 scopes example:
  - read:users - Read user data
  - write:users - Write user data
  - admin - Admin access

In FastAPI:
  from fastapi.security import SecurityScopes
  
  async def get_current_user(
      security_scopes: SecurityScopes,
      token: str = Depends(oauth2_scheme)
  ):
      # Check scopes
      pass
""")

print("\n=== Security Best Practices ===")

best_practices = [
    "Use HTTPS in production",
    "Store secret keys in environment variables",
    "Use strong password hashing (bcrypt)",
    "Set appropriate token expiration times",
    "Implement token refresh mechanism",
    "Validate all user inputs",
    "Use secure session management",
    "Implement rate limiting",
    "Log authentication attempts",
    "Use OAuth2 scopes for fine-grained access"
]

print("Security best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Testing Authentication ===")

print("""
1. Register a user:
   POST /register?username=test&password=test123&email=test@example.com

2. Login to get token:
   POST /token
   Form data: username=test, password=test123
   Response: {"access_token": "...", "token_type": "bearer"}

3. Access protected route:
   GET /users/me
   Header: Authorization: Bearer <token>

4. Refresh token:
   POST /refresh
   Header: Authorization: Bearer <token>
""")

print("\n=== Running the Application ===")
print("""
To run this FastAPI application:

1. Install dependencies:
   pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart

2. Run the server:
   uvicorn main:app --reload

3. Test authentication:
   - Register: POST /register
   - Login: POST /token
   - Access protected: GET /users/me (with token)
""")

if __name__ == "__main__":
    import uvicorn
    print("\nStarting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

