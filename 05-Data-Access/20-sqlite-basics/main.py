# SQLite Basics in Python

import sqlite3
import os

# Remove existing database if it exists
db_file = "example.db"
if os.path.exists(db_file):
    os.remove(db_file)

print("=== Creating Database and Table ===")

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

print("Table 'users' created successfully")

# Commit the transaction
conn.commit()

print("\n=== Inserting Data ===")

# Insert single record
cursor.execute("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", ("Alice", "alice@example.com", 30))

print("Inserted: Alice")

# Insert multiple records
users_data = [
    ("Bob", "bob@example.com", 25),
    ("Charlie", "charlie@example.com", 35),
    ("Diana", "diana@example.com", 28)
]

cursor.executemany("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", users_data)

print(f"Inserted {len(users_data)} more users")
conn.commit()

print("\n=== Querying Data ===")

# Select all records
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("All users:")
for user in all_users:
    print(f"  ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

# Select with WHERE clause
cursor.execute("SELECT * FROM users WHERE age > ?", (27,))
older_users = cursor.fetchall()

print("\nUsers older than 27:")
for user in older_users:
    print(f"  {user[1]} ({user[3]} years old)")

# Select specific columns
cursor.execute("SELECT name, email FROM users")
user_info = cursor.fetchall()

print("\nUser names and emails:")
for name, email in user_info:
    print(f"  {name}: {email}")

print("\n=== Fetching Methods ===")

# fetchone() - get single row
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
user = cursor.fetchone()
print(f"Single user (fetchone): {user}")

# fetchmany() - get specified number of rows
cursor.execute("SELECT * FROM users LIMIT 2")
two_users = cursor.fetchmany(2)
print(f"Two users (fetchmany): {two_users}")

# fetchall() - get all rows
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"Total users: {count}")

print("\n=== Updating Data ===")

# Update record
cursor.execute("""
    UPDATE users
    SET age = ?
    WHERE name = ?
""", (31, "Alice"))

conn.commit()
print("Updated Alice's age to 31")

# Verify update
cursor.execute("SELECT name, age FROM users WHERE name = ?", ("Alice",))
updated_user = cursor.fetchone()
print(f"Updated user: {updated_user}")

print("\n=== Deleting Data ===")

# Delete record
cursor.execute("DELETE FROM users WHERE name = ?", ("Charlie",))
conn.commit()
print("Deleted user: Charlie")

# Verify deletion
cursor.execute("SELECT COUNT(*) FROM users")
remaining = cursor.fetchone()[0]
print(f"Remaining users: {remaining}")

print("\n=== Parameterized Queries (Security) ===")

# Safe way - using parameters
name_to_find = "Bob"
cursor.execute("SELECT * FROM users WHERE name = ?", (name_to_find,))
safe_result = cursor.fetchone()
print(f"Safe query result: {safe_result}")

# Never do this (SQL injection risk):
# cursor.execute(f"SELECT * FROM users WHERE name = '{name_to_find}'")

print("\n=== Transactions ===")

# Start transaction
try:
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Eve", "eve@example.com", 22))
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Frank", "frank@example.com", 40))
    conn.commit()
    print("Transaction committed: Added Eve and Frank")
except sqlite3.Error as e:
    conn.rollback()
    print(f"Transaction rolled back: {e}")

# Demonstrate rollback
try:
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                   ("Alice", "alice@example.com", 30))  # Duplicate email
    conn.commit()
except sqlite3.IntegrityError as e:
    conn.rollback()
    print(f"Transaction rolled back due to constraint violation: {e}")

print("\n=== Using Context Manager ===")

# Using connection as context manager
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Users in database (using context manager): {count}")

print("\n=== Creating Multiple Tables ===")

# Create additional table
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    
    # Create posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    # Insert posts
    cursor.execute("SELECT id FROM users WHERE name = ?", ("Alice",))
    alice_id = cursor.fetchone()[0]
    
    cursor.execute("""
        INSERT INTO posts (user_id, title, content)
        VALUES (?, ?, ?)
    """, (alice_id, "My First Post", "This is the content of my first post"))
    
    conn.commit()
    print("Created posts table and inserted a post")

print("\n=== Joining Tables ===")

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    
    # Inner join
    cursor.execute("""
        SELECT users.name, posts.title, posts.content
        FROM users
        INNER JOIN posts ON users.id = posts.user_id
    """)
    
    joined_results = cursor.fetchall()
    print("Users and their posts:")
    for name, title, content in joined_results:
        print(f"  {name}: {title} - {content}")

print("\n=== Database Schema Information ===")

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Get table schema
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    print("\nUsers table schema:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")

print("\n=== Row Factory (Dictionary-like Access) ===")

# Set row factory for dictionary-like access
conn = sqlite3.connect(db_file)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
row = cursor.fetchone()

print("Dictionary-like access:")
print(f"  row['name']: {row['name']}")
print(f"  row['email']: {row['email']}")
print(f"  row['age']: {row['age']}")

conn.close()

print("\n=== Error Handling ===")

def safe_query(db_file, query, params=None):
    """Safely execute a query with error handling"""
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

result = safe_query(db_file, "SELECT * FROM users WHERE age > ?", (25,))
if result:
    print(f"Query successful: {len(result)} results")

# Clean up - ensure all connections are closed
import time
time.sleep(0.1)  # Give time for connections to close
if os.path.exists(db_file):
    try:
        os.remove(db_file)
        print(f"\nDatabase file '{db_file}' removed")
    except PermissionError:
        print(f"\nNote: Database file '{db_file}' is in use and will be cleaned up later")

