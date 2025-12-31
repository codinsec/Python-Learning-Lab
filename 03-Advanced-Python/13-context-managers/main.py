# Context Managers in Python

from contextlib import contextmanager
import os

print("=== Built-in Context Manager (File) ===")

# File context manager automatically closes file
with open("temp_file.txt", "w") as f:
    f.write("Hello, Context Manager!")

# File is automatically closed after with block
print("File written and closed")

# Read the file
with open("temp_file.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

# Clean up
os.remove("temp_file.txt")

print("\n=== Custom Context Manager (Class-Based) ===")

class FileManager:
    """Custom context manager for file operations"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering with block"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block"""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions, True to suppress
        return False

# Use custom context manager
with FileManager("temp_file2.txt", "w") as f:
    f.write("Custom context manager!")

# File is automatically closed
print("File closed automatically")

# Clean up
if os.path.exists("temp_file2.txt"):
    os.remove("temp_file2.txt")

print("\n=== Context Manager with Exception Handling ===")

class Timer:
    """Context manager that measures execution time"""
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"{self.name} started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start_time
        print(f"{self.name} completed in {elapsed:.4f} seconds")
        return False

with Timer("Data processing"):
    # Simulate some work
    import time
    time.sleep(0.1)
    print("Processing data...")

print("\n=== Context Manager with State ===")

class DatabaseConnection:
    """Context manager for database connections"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to {self.host}:{self.port}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from {self.host}:{self.port}")
        self.connected = False
        return False
    
    def execute(self, query):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing: {query}")

with DatabaseConnection("localhost", 5432) as db:
    db.execute("SELECT * FROM users")

print("\n=== Using @contextmanager Decorator ===")

@contextmanager
def file_manager(filename, mode):
    """Context manager using generator function"""
    print(f"Opening {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        file.close()

with file_manager("temp_file3.txt", "w") as f:
    f.write("Using @contextmanager decorator!")

# Clean up
if os.path.exists("temp_file3.txt"):
    os.remove("temp_file3.txt")

print("\n=== Context Manager for Resource Locking ===")

@contextmanager
def lock_resource(resource_name):
    """Context manager that locks a resource"""
    print(f"Locking {resource_name}")
    try:
        yield resource_name
    finally:
        print(f"Unlocking {resource_name}")

with lock_resource("database"):
    print("Performing database operations...")

print("\n=== Multiple Context Managers ===")

class Indenter:
    """Context manager for indentation"""
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        return False
    
    def print(self, text):
        print("  " * self.level + text)

with Indenter() as indent:
    indent.print("Level 1")
    with indent:
        indent.print("Level 2")
        with indent:
            indent.print("Level 3")
    indent.print("Back to Level 1")

print("\n=== Context Manager with Error Suppression ===")

class SuppressErrors:
    """Context manager that suppresses specific exceptions"""
    def __init__(self, *exceptions):
        self.exceptions = exceptions
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions):
            print(f"Suppressed {exc_type.__name__}: {exc_val}")
            return True  # Suppress the exception
        return False  # Don't suppress other exceptions

with SuppressErrors(ValueError, KeyError):
    raise ValueError("This error will be suppressed")

print("Code continues after suppressed error")

print("\n=== Context Manager for Temporary Directory ===")

@contextmanager
def temporary_directory():
    """Context manager for temporary directory"""
    import tempfile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    try:
        yield temp_dir
    finally:
        print(f"Removing temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir)

with temporary_directory() as temp_dir:
    print(f"Working in: {temp_dir}")
    # Create a file in temp directory
    temp_file = os.path.join(temp_dir, "test.txt")
    with open(temp_file, "w") as f:
        f.write("Test content")

print("Temporary directory cleaned up")

