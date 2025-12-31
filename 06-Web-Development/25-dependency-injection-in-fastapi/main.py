# Dependency Injection in FastAPI

from fastapi import FastAPI, Depends, Query, HTTPException, Header
from typing import Optional

app = FastAPI(title="Dependency Injection Examples")

print("=== FastAPI Dependency Injection ===")
print("To run: uvicorn main:app --reload")

print("\n=== Basic Function Dependency ===")

def get_common_params(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Common pagination dependency"""
    return {"skip": skip, "limit": limit}

@app.get("/items")
async def get_items(params: dict = Depends(get_common_params)):
    """Get items with pagination dependency"""
    return {
        "items": [f"item_{i}" for i in range(params["skip"], params["skip"] + params["limit"])],
        "skip": params["skip"],
        "limit": params["limit"]
    }

print("""
Example:
  GET /items?skip=0&limit=5
  Uses get_common_params dependency for pagination
""")

print("\n=== Class-Based Dependency ===")

class Pagination:
    def __init__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100)
    ):
        self.skip = skip
        self.limit = limit

@app.get("/products")
async def get_products(pagination: Pagination = Depends()):
    """Get products with class-based pagination"""
    return {
        "products": [f"product_{i}" for i in range(pagination.skip, pagination.skip + pagination.limit)],
        "pagination": {"skip": pagination.skip, "limit": pagination.limit}
    }

print("""
Example:
  GET /products?skip=10&limit=20
  Uses Pagination class dependency
""")

print("\n=== Sub-Dependencies ===")

def get_query_token(token: str = Query(...)):
    """Sub-dependency for token"""
    if token != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    return token

def get_query_skip_limit(q: str = Query(None), token: str = Depends(get_query_token)):
    """Dependency that uses another dependency"""
    return {"q": q, "token": token}

@app.get("/protected")
async def protected_route(params: dict = Depends(get_query_skip_limit)):
    """Route with sub-dependency"""
    return {"message": "Protected route accessed", "params": params}

print("""
Example:
  GET /protected?token=secret-token&q=search
  Uses sub-dependency chain
""")

print("\n=== Database Session Dependency (Example) ===")

class Database:
    def __init__(self):
        self.data = {"users": [], "items": []}
    
    def get_session(self):
        """Simulate database session"""
        return self

db = Database()

def get_db():
    """Dependency for database session"""
    session = db.get_session()
    try:
        yield session
    finally:
        # Cleanup if needed
        pass

@app.get("/db-items")
async def get_db_items(database: Database = Depends(get_db)):
    """Get items using database dependency"""
    return {"items": database.data["items"]}

print("""
Example:
  GET /db-items
  Uses database session dependency
""")

print("\n=== Authentication Dependency ===")

def verify_token(authorization: Optional[str] = Header(None)):
    """Verify authentication token"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization format")
    
    token = authorization.replace("Bearer ", "")
    if token != "valid-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    
    return {"user_id": 1, "username": "alice"}

@app.get("/protected-route")
async def protected_route(user: dict = Depends(verify_token)):
    """Protected route requiring authentication"""
    return {"message": f"Hello {user['username']}", "user": user}

print("""
Example:
  GET /protected-route
  Header: Authorization: Bearer valid-token
""")

print("\n=== Multiple Dependencies ===")

def get_pagination(skip: int = Query(0), limit: int = Query(10)):
    return {"skip": skip, "limit": limit}

def get_filter(search: Optional[str] = Query(None)):
    return {"search": search}

@app.get("/filtered-items")
async def get_filtered_items(
    pagination: dict = Depends(get_pagination),
    filter_params: dict = Depends(get_filter)
):
    """Route with multiple dependencies"""
    return {
        "items": [f"item_{i}" for i in range(pagination["skip"], pagination["skip"] + pagination["limit"])],
        "pagination": pagination,
        "filter": filter_params
    }

print("""
Example:
  GET /filtered-items?skip=0&limit=5&search=test
  Uses multiple dependencies
""")

print("\n=== Dependency with State ===")

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

counter = Counter()

def get_counter():
    """Dependency that maintains state"""
    return counter

@app.get("/count")
async def get_count(counter: Counter = Depends(get_counter)):
    """Get and increment counter"""
    count = counter.increment()
    return {"count": count}

print("""
Example:
  GET /count - Returns incremented count each time
""")

print("\n=== Optional Dependencies ===")

def get_optional_header(x_custom_header: Optional[str] = Header(None)):
    """Optional dependency"""
    return x_custom_header

@app.get("/optional")
async def optional_route(header: Optional[str] = Depends(get_optional_header)):
    """Route with optional dependency"""
    if header:
        return {"message": f"Header provided: {header}"}
    return {"message": "No header provided"}

print("""
Example:
  GET /optional
  GET /optional (with X-Custom-Header: value)
""")

print("\n=== Dependency Override (Testing) ===")

def get_test_db():
    """Test database dependency"""
    return {"test": True, "data": "test_data"}

# In tests, you can override dependencies:
# app.dependency_overrides[get_db] = get_test_db

print("""
Dependency override pattern for testing:
  app.dependency_overrides[original_dependency] = test_dependency
""")

print("\n=== Common Dependency Patterns ===")

# Pattern 1: Pagination
def pagination_params(skip: int = Query(0), limit: int = Query(10)):
    return {"skip": skip, "limit": limit}

# Pattern 2: Sorting
def sorting_params(sort_by: Optional[str] = Query(None), order: str = Query("asc")):
    return {"sort_by": sort_by, "order": order}

# Pattern 3: Filtering
def filtering_params(
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None)
):
    return {"min_price": min_price, "max_price": max_price}

@app.get("/advanced-search")
async def advanced_search(
    pagination: dict = Depends(pagination_params),
    sorting: dict = Depends(sorting_params),
    filtering: dict = Depends(filtering_params)
):
    """Route using multiple common patterns"""
    return {
        "pagination": pagination,
        "sorting": sorting,
        "filtering": filtering
    }

print("""
Example:
  GET /advanced-search?skip=0&limit=10&sort_by=price&order=desc&min_price=10&max_price=100
""")

print("\n=== Running the Application ===")
print("""
To run this FastAPI application:

1. Install dependencies:
   pip install fastapi uvicorn

2. Run the server:
   uvicorn main:app --reload

3. Test endpoints:
   - GET /items?skip=0&limit=5
   - GET /products?skip=10&limit=20
   - GET /protected?token=secret-token
   - GET /protected-route (with Authorization header)
   - GET /count (multiple times to see increment)
""")

if __name__ == "__main__":
    import uvicorn
    print("\nStarting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

