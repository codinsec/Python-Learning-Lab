# Logging and Configuration in Python

import logging
import os
from datetime import datetime

print("=== Basic Logging ===")

# Basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("\n=== Log Levels ===")

log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

print("Log levels (from lowest to highest):")
for level_name, level_value in log_levels.items():
    print(f"  {level_name}: {level_value}")

print("\n=== Custom Logger Configuration ===")

# Create custom logger
custom_logger = logging.getLogger("my_app")
custom_logger.setLevel(logging.DEBUG)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler.setFormatter(formatter)

# Add handler to logger
custom_logger.addHandler(console_handler)

custom_logger.debug("Debug message (won't show)")
custom_logger.info("Info message")
custom_logger.warning("Warning message")

print("\n=== File Logging ===")

# Setup file logging
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Formatter for file
file_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(file_formatter)

file_logger.addHandler(file_handler)

# Log to file
file_logger.info("This message goes to file")
file_logger.warning("Warning also logged to file")

print("Check app.log file for logged messages")

# Close handler and clean up
file_handler.close()
file_logger.removeHandler(file_handler)
if os.path.exists("app.log"):
    os.remove("app.log")

print("\n=== Multiple Handlers ===")

multi_logger = logging.getLogger("multi_handler")
multi_logger.setLevel(logging.DEBUG)

# Console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# File handler
file = logging.FileHandler("multi.log")
file.setLevel(logging.DEBUG)

# Formatters
console_format = logging.Formatter('%(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console.setFormatter(console_format)
file.setFormatter(file_format)

multi_logger.addHandler(console)
multi_logger.addHandler(file)

multi_logger.info("This appears in both console and file")
multi_logger.debug("This appears only in file")

# Close handlers and clean up
console.close()
file.close()
multi_logger.removeHandler(console)
multi_logger.removeHandler(file)
if os.path.exists("multi.log"):
    os.remove("multi.log")

print("\n=== Environment Variables ===")

# Get environment variables
print("Environment variables:")
print(f"  USER: {os.environ.get('USER', 'Not set')}")
print(f"  PATH exists: {bool(os.environ.get('PATH'))}")

# Set environment variable (for current process)
os.environ['MY_APP_DEBUG'] = 'true'
print(f"  MY_APP_DEBUG: {os.environ.get('MY_APP_DEBUG')}")

print("\n=== .env File Pattern ===")

# Example .env file content
env_content = """# Application Configuration
DEBUG=true
DATABASE_URL=postgresql://localhost/mydb
API_KEY=your-secret-key-here
LOG_LEVEL=INFO
"""

print("Example .env file content:")
print(env_content)

print("""
To use .env files, install python-dotenv:
  pip install python-dotenv

Then in your code:
  from dotenv import load_dotenv
  load_dotenv()
  
  debug = os.getenv('DEBUG', 'false')
""")

print("\n=== Configuration Management ===")

class Config:
    """Simple configuration class"""
    def __init__(self):
        self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.api_key = os.getenv('API_KEY', '')
    
    def __repr__(self):
        return f"Config(debug={self.debug}, log_level={self.log_level})"

config = Config()
print(f"Configuration: {config}")

print("\n=== Logging Configuration from Config ===")

def setup_logging_from_config(config):
    """Setup logging based on configuration"""
    log_level = getattr(logging, config.log_level.upper(), logging.INFO)
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logger = logging.getLogger(__name__)
    return logger

app_logger = setup_logging_from_config(config)
app_logger.info("Logger configured from config")
app_logger.debug("Debug message (may not show based on level)")

print("\n=== Structured Logging Example ===")

def log_user_action(logger, user_id, action, status="success"):
    """Example of structured logging"""
    logger.info(
        f"User action - user_id: {user_id}, action: {action}, status: {status}",
        extra={
            'user_id': user_id,
            'action': action,
            'status': status
        }
    )

action_logger = logging.getLogger("user_actions")
action_logger.info("User logged in - user_id: 123, action: login, status: success")

print("\n=== Log Rotation (Conceptual) ===")

print("""
For production, use RotatingFileHandler or TimedRotatingFileHandler:

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'app.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5
)
logger.addHandler(handler)
""")

print("\n=== Best Practices ===")

best_practices = [
    "Use appropriate log levels",
    "Don't log sensitive information (passwords, tokens)",
    "Use structured logging for better analysis",
    "Configure different log levels for development and production",
    "Use log rotation for file handlers",
    "Include context in log messages",
    "Use separate loggers for different modules"
]

print("Logging best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Configuration File Pattern ===")

config_file_example = """# config.py
import os

class DevelopmentConfig:
    DEBUG = True
    DATABASE_URL = 'sqlite:///dev.db'
    LOG_LEVEL = 'DEBUG'

class ProductionConfig:
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')
    LOG_LEVEL = 'INFO'

# Select config based on environment
config = DevelopmentConfig if os.getenv('FLASK_ENV') == 'development' else ProductionConfig
"""

print("Example configuration pattern:")
print(config_file_example)

