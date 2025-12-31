# Middleware and CORS in FastAPI

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI(title="Middleware and CORS Examples")

print("=== FastAPI Middleware and CORS ===")
print("To run: uvicorn main:app --reload")

print("\n=== CORS Configuration ===")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allowed headers
)

print("""
CORS configured to allow:
  - Origins: http://localhost:3000, http://localhost:8080
  - Credentials: True
  - Methods: All
  - Headers: All
""")

print("\n=== Custom Middleware ===")

class TimingMiddleware(BaseHTTPMiddleware):
    """Custom middleware to measure request processing time"""
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Process request
        response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Add custom header
        response.headers["X-Process-Time"] = str(process_time)
        
        return response

app.add_middleware(TimingMiddleware)

print("""
Custom middleware added:
  - Measures request processing time
  - Adds X-Process-Time header to response
""")

print("\n=== Logging Middleware ===")

class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for request logging"""
    async def dispatch(self, request: Request, call_next):
        # Log request
        print(f"Request: {request.method} {request.url}")
        
        # Process request
        response = await call_next(request)
        
        # Log response
        print(f"Response: {response.status_code}")
        
        return response

app.add_middleware(LoggingMiddleware)

print("""
Logging middleware added:
  - Logs request method and URL
  - Logs response status code
""")

print("\n=== Authentication Middleware (Example) ===")

class AuthMiddleware(BaseHTTPMiddleware):
    """Example authentication middleware"""
    async def dispatch(self, request: Request, call_next):
        # Skip auth for certain paths
        if request.url.path in ["/", "/docs", "/openapi.json"]:
            return await call_next(request)
        
        # Check authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            from fastapi import Response
            return Response(
                content='{"detail": "Authorization required"}',
                status_code=401,
                media_type="application/json"
            )
        
        # Process request
        response = await call_next(request)
        return response

# Uncomment to enable auth middleware
# app.add_middleware(AuthMiddleware)

print("""
Authentication middleware example (commented out):
  - Checks Authorization header
  - Allows public paths
  - Returns 401 if not authenticated
""")

print("\n=== Trusted Host Middleware ===")

# Only allow requests from specific hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "*.example.com"]
)

print("""
Trusted host middleware configured:
  - Only allows requests from: localhost, 127.0.0.1, *.example.com
""")

print("\n=== Basic Routes ===")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Middleware and CORS example"}

@app.get("/test")
async def test():
    """Test endpoint"""
    return {"message": "Test endpoint", "cors_enabled": True}

@app.post("/data")
async def create_data(data: dict):
    """POST endpoint to test CORS"""
    return {"message": "Data created", "received": data}

print("""
Routes defined:
  GET  / - Root
  GET  /test - Test endpoint
  POST /data - Create data (tests CORS)
""")

print("\n=== CORS Configuration Options ===")

cors_options = {
    "allow_origins": ["http://localhost:3000"],
    "allow_origin_regex": "https://.*\\.example\\.com",
    "allow_methods": ["GET", "POST"],
    "allow_headers": ["Content-Type", "Authorization"],
    "allow_credentials": True,
    "expose_headers": ["X-Custom-Header"],
    "max_age": 3600
}

print("""
CORS configuration options:
  - allow_origins: List of allowed origins
  - allow_origin_regex: Regex pattern for origins
  - allow_methods: Allowed HTTP methods
  - allow_headers: Allowed request headers
  - allow_credentials: Allow credentials
  - expose_headers: Headers to expose to client
  - max_age: Cache preflight requests
""")

print("\n=== Middleware Execution Order ===")

print("""
Middleware executes in reverse order of addition:
  1. Last added middleware runs first (on request)
  2. First added middleware runs last (on response)
  
Example:
  app.add_middleware(Middleware1)  # Runs last
  app.add_middleware(Middleware2)  # Runs first
""")

print("\n=== Request Modification Middleware ===")

class RequestModificationMiddleware(BaseHTTPMiddleware):
    """Middleware that modifies request"""
    async def dispatch(self, request: Request, call_next):
        # Add custom attribute to request
        request.state.custom_data = "Modified by middleware"
        
        response = await call_next(request)
        return response

app.add_middleware(RequestModificationMiddleware)

@app.get("/middleware-data")
async def get_middleware_data(request: Request):
    """Access middleware-modified request"""
    return {"custom_data": getattr(request.state, "custom_data", None)}

print("""
Request modification middleware:
  - Adds custom_data to request.state
  - Accessible in route handlers
""")

print("\n=== Response Modification Middleware ===")

class ResponseModificationMiddleware(BaseHTTPMiddleware):
    """Middleware that modifies response"""
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Add custom header
        response.headers["X-Custom-Header"] = "Modified by middleware"
        
        return response

app.add_middleware(ResponseModificationMiddleware)

print("""
Response modification middleware:
  - Adds X-Custom-Header to all responses
""")

print("\n=== Error Handling Middleware ===")

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """Middleware for error handling"""
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            from fastapi.responses import JSONResponse
            return JSONResponse(
                status_code=500,
                content={"detail": f"Internal server error: {str(e)}"}
            )

# Uncomment to enable error handling middleware
# app.add_middleware(ErrorHandlingMiddleware)

print("""
Error handling middleware example (commented out):
  - Catches exceptions
  - Returns formatted error response
""")

print("\n=== CORS Preflight Requests ===")

print("""
CORS preflight (OPTIONS) requests are handled automatically:
  - Browser sends OPTIONS request before actual request
  - FastAPI responds with allowed methods/headers
  - Browser then sends actual request if allowed
""")

print("\n=== Testing CORS ===")

print("""
To test CORS from browser console:

fetch('http://localhost:8000/test', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data));
""")

print("\n=== Running the Application ===")
print("""
To run this FastAPI application:

1. Install dependencies:
   pip install fastapi uvicorn

2. Run the server:
   uvicorn main:app --reload

3. Test CORS:
   - Open browser console on http://localhost:3000
   - Make fetch request to http://localhost:8000/test
   - Check response headers for CORS headers

4. Check middleware:
   - Look for X-Process-Time header in responses
   - Check console for request/response logs
""")

if __name__ == "__main__":
    import uvicorn
    print("\nStarting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

