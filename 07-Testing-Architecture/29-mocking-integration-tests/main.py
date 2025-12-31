# Code to be tested with mocking

import time
import requests

def fetch_user_data(user_id):
    """Fetch user data from external API"""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

def process_payment(amount, card_number):
    """Process payment (would call external service)"""
    # Simulate external API call
    time.sleep(0.1)  # Simulate network delay
    return {"status": "success", "transaction_id": "12345"}

def send_email(to, subject, body):
    """Send email (would call email service)"""
    # Simulate email sending
    print(f"Sending email to {to}: {subject}")
    return True

class Database:
    """Database class for testing"""
    def __init__(self):
        self.data = {}
    
    def save(self, key, value):
        """Save data to database"""
        self.data[key] = value
        return True
    
    def get(self, key):
        """Get data from database"""
        return self.data.get(key)

class UserService:
    """User service that depends on Database"""
    def __init__(self, db):
        self.db = db
    
    def create_user(self, username, email):
        """Create user using database"""
        user_data = {"username": username, "email": email}
        self.db.save(username, user_data)
        return user_data
    
    def get_user(self, username):
        """Get user from database"""
        return self.db.get(username)

