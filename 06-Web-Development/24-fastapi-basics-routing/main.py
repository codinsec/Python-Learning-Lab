# FastAPI Basics and Routing

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse

# Create FastAPI app instance
app = FastAPI(
    title="Python Learning Lab API",
    description="FastAPI basics and routing examples",
    version="1.0.0"
)

print("=== FastAPI Application Created ===")
print("To run: uvicorn main:app --reload")
print("API Docs: http://localhost:8000/docs")

# In-memory data store (for demonstration)
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

print("\n=== Basic Routes ===")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Learning Lab"}

@app.get("/hello")
async def hello():
    """Simple GET endpoint"""
    return {"message": "Hello, FastAPI!"}

print("""
Example routes defined:
  GET / - Root endpoint
  GET /hello - Hello endpoint
""")

print("\n=== Path Parameters ===")

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get user by ID (path parameter)"""
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str = None):
    """Get item with optional query parameter"""
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    return result

print("""
Path parameters example:
  GET /users/1 - Get user with ID 1
  GET /items/5?q=search - Get item 5 with query parameter
""")

print("\n=== Query Parameters ===")

@app.get("/search")
async def search(
    q: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(10, ge=1, le=100, description="Result limit"),
    skip: int = Query(0, ge=0, description="Skip results")
):
    """Search endpoint with query parameters"""
    return {
        "query": q,
        "limit": limit,
        "skip": skip,
        "results": f"Searching for '{q}' with limit {limit}, skipping {skip}"
    }

print("""
Query parameters example:
  GET /search?q=python&limit=20&skip=0
""")

print("\n=== POST Request with Body ===")

@app.post("/users")
async def create_user(user: dict):
    """Create a new user"""
    new_id = max([u["id"] for u in users_db], default=0) + 1
    new_user = {
        "id": new_id,
        "name": user.get("name"),
        "email": user.get("email")
    }
    users_db.append(new_user)
    return {"message": "User created", "user": new_user}

print("""
POST request example:
  POST /users
  Body: {"name": "Diana", "email": "diana@example.com"}
""")

print("\n=== PUT Request (Update) ===")

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: dict):
    """Update user by ID"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_index].update({
        "name": user.get("name", users_db[user_index]["name"]),
        "email": user.get("email", users_db[user_id]["email"])
    })
    return {"message": "User updated", "user": users_db[user_index]}

print("""
PUT request example:
  PUT /users/1
  Body: {"name": "Alice Updated", "email": "alice.new@example.com"}
""")

print("\n=== DELETE Request ===")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete user by ID"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_index)
    return {"message": "User deleted", "user": deleted_user}

print("""
DELETE request example:
  DELETE /users/1
""")

print("\n=== Status Codes ===")

@app.post("/items", status_code=201)
async def create_item(item: dict):
    """Create item with custom status code"""
    return {"message": "Item created", "item": item}

@app.get("/items/{item_id}", status_code=200)
async def get_item_status(item_id: int):
    """Get item with explicit status code"""
    return {"item_id": item_id, "status": "found"}

print("""
Status codes:
  200 - OK (default for GET)
  201 - Created (for POST)
  404 - Not Found
  400 - Bad Request
""")

print("\n=== Error Handling ===")

@app.get("/error-example")
async def error_example():
    """Example of raising HTTP exception"""
    raise HTTPException(
        status_code=400,
        detail="This is an example error",
        headers={"X-Error": "Example"}
    )

print("\n=== Response Models ===")

@app.get("/users", response_model=dict)
async def get_all_users():
    """Get all users with response model"""
    return {"users": users_db, "count": len(users_db)}

print("""
Response models help with:
  - Automatic validation
  - API documentation
  - Type checking
""")

print("\n=== Path Validation ===")

@app.get("/users/{user_id}/posts/{post_id}")
async def get_user_post(
    user_id: int = Path(..., gt=0, description="User ID"),
    post_id: int = Path(..., gt=0, description="Post ID")
):
    """Get user's post with path validation"""
    return {
        "user_id": user_id,
        "post_id": post_id,
        "message": f"Post {post_id} by user {user_id}"
    }

print("""
Path validation example:
  GET /users/1/posts/5 - Valid
  GET /users/0/posts/5 - Invalid (user_id must be > 0)
""")

print("\n=== Multiple HTTP Methods ===")

@app.get("/items/{item_id}")
async def get_item_method(item_id: int):
    """GET item"""
    return {"item_id": item_id, "method": "GET"}

@app.post("/items/{item_id}")
async def create_item_method(item_id: int, item: dict):
    """POST to item"""
    return {"item_id": item_id, "method": "POST", "item": item}

@app.put("/items/{item_id}")
async def update_item_method(item_id: int, item: dict):
    """PUT item"""
    return {"item_id": item_id, "method": "PUT", "item": item}

@app.delete("/items/{item_id}")
async def delete_item_method(item_id: int):
    """DELETE item"""
    return {"item_id": item_id, "method": "DELETE"}

print("""
Same path, different methods:
  GET /items/1
  POST /items/1
  PUT /items/1
  DELETE /items/1
""")

print("\n=== Custom Response ===")

@app.get("/custom-response")
async def custom_response():
    """Return custom JSON response"""
    return JSONResponse(
        status_code=200,
        content={"message": "Custom response", "data": {"key": "value"}}
    )

print("\n=== Route Summary ===")

print("""
All routes defined:
  GET  / - Root
  GET  /hello - Hello message
  GET  /users - Get all users
  GET  /users/{user_id} - Get user by ID
  POST /users - Create user
  PUT  /users/{user_id} - Update user
  DELETE /users/{user_id} - Delete user
  GET  /search - Search with query params
  GET  /items/{item_id} - Get item
  POST /items - Create item
  GET  /users/{user_id}/posts/{post_id} - Get user post
""")

print("\n=== Running the Application ===")
print("""
To run this FastAPI application:

1. Install dependencies:
   pip install fastapi uvicorn

2. Run the server:
   uvicorn main:app --reload

3. Access:
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

4. Test endpoints:
   - curl http://localhost:8000/
   - curl http://localhost:8000/users/1
   - curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"name":"Test","email":"test@example.com"}'
""")

if __name__ == "__main__":
    import uvicorn
    print("\nStarting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

