# SQLAlchemy ORM in Python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

# Remove existing database
db_file = "orm_example.db"
if os.path.exists(db_file):
    os.remove(db_file)

# Create engine
engine = create_engine(f'sqlite:///{db_file}', echo=False)

# Base class for models
Base = declarative_base()

print("=== Defining Models ===")

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship
    author = relationship("User", back_populates="posts")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"

# Create tables
Base.metadata.create_all(engine)
print("Tables created successfully")

print("\n=== Creating Session ===")

# Create session factory
Session = sessionmaker(bind=engine)
session = Session()

print("\n=== Creating Records (INSERT) ===")

# Create users
user1 = User(name="Alice", email="alice@example.com", age=30)
user2 = User(name="Bob", email="bob@example.com", age=25)
user3 = User(name="Charlie", email="charlie@example.com", age=35)

# Add to session
session.add(user1)
session.add(user2)
session.add(user3)

# Commit to database
session.commit()
print("Created 3 users")

# Create posts
post1 = Post(title="First Post", content="Content of first post", user_id=user1.id)
post2 = Post(title="Second Post", content="Content of second post", user_id=user1.id)
post3 = Post(title="Bob's Post", content="Bob's content", user_id=user2.id)

session.add_all([post1, post2, post3])
session.commit()
print("Created 3 posts")

print("\n=== Querying Records (SELECT) ===")

# Get all users
all_users = session.query(User).all()
print("All users:")
for user in all_users:
    print(f"  {user}")

# Get user by ID
user = session.query(User).filter(User.id == 1).first()
print(f"\nUser with ID 1: {user}")

# Get users with filter
young_users = session.query(User).filter(User.age < 30).all()
print("\nUsers younger than 30:")
for user in young_users:
    print(f"  {user.name} ({user.age} years)")

# Get single user by email
alice = session.query(User).filter(User.email == "alice@example.com").first()
print(f"\nUser by email: {alice}")

print("\n=== Using Relationships ===")

# Access posts through relationship
print(f"\n{user1.name}'s posts:")
for post in user1.posts:
    print(f"  - {post.title}")

# Access author through relationship
print(f"\nPost '{post1.title}' author: {post1.author.name}")

print("\n=== Updating Records (UPDATE) ===")

# Update user
user1.age = 31
session.commit()
print(f"Updated {user1.name}'s age to {user1.age}")

# Update using query
session.query(User).filter(User.name == "Bob").update({"age": 26})
session.commit()
print("Updated Bob's age to 26")

print("\n=== Deleting Records (DELETE) ===")

# Delete a post
post_to_delete = session.query(Post).filter(Post.title == "Second Post").first()
if post_to_delete:
    session.delete(post_to_delete)
    session.commit()
    print("Deleted 'Second Post'")

# Verify deletion
remaining_posts = session.query(Post).count()
print(f"Remaining posts: {remaining_posts}")

print("\n=== Advanced Queries ===")

# Count
user_count = session.query(User).count()
print(f"Total users: {user_count}")

# Order by
users_by_age = session.query(User).order_by(User.age.desc()).all()
print("\nUsers ordered by age (descending):")
for user in users_by_age:
    print(f"  {user.name}: {user.age}")

# Limit
first_two = session.query(User).limit(2).all()
print(f"\nFirst 2 users: {[u.name for u in first_two]}")

# Multiple filters
result = session.query(User).filter(
    User.age > 25,
    User.age < 35
).all()
print("\nUsers between 25 and 35:")
for user in result:
    print(f"  {user.name}: {user.age}")

print("\n=== Joins ===")

# Join query
users_with_posts = session.query(User, Post).join(Post).all()
print("Users with their posts:")
for user, post in users_with_posts:
    print(f"  {user.name}: {post.title}")

print("\n=== Query with Relationships ===")

# Get users who have posts
users_with_posts = session.query(User).join(Post).distinct().all()
print("\nUsers who have posts:")
for user in users_with_posts:
    print(f"  {user.name}")

print("\n=== Using Relationships for Filtering ===")

# Get posts by user name
alice_posts = session.query(Post).join(User).filter(User.name == "Alice").all()
print("\nAlice's posts:")
for post in alice_posts:
    print(f"  - {post.title}")

print("\n=== Session Management ===")

# Create new session
new_session = Session()

try:
    new_user = User(name="Diana", email="diana@example.com", age=28)
    new_session.add(new_user)
    new_session.commit()
    print("\nAdded new user: Diana")
except Exception as e:
    new_session.rollback()
    print(f"Error: {e}")
finally:
    new_session.close()

print("\n=== Querying with Relationships ===")

# Eager loading (using joinedload would require additional import)
users = session.query(User).all()
print("\nUsers and their post counts:")
for user in users:
    print(f"  {user.name}: {len(user.posts)} posts")

print("\n=== Model Methods ===")

# Add method to User model
class UserWithMethods(Base):
    __tablename__ = 'users_with_methods'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    def get_display_name(self):
        return f"{self.name} ({self.email})"

# Note: This would require recreating the table, so it's just for demonstration
print("Models can have custom methods for business logic")

print("\n=== Transactions ===")

try:
    user4 = User(name="Eve", email="eve@example.com", age=22)
    session.add(user4)
    
    # Intentionally create duplicate to demonstrate rollback
    user5 = User(name="Frank", email="alice@example.com", age=40)  # Duplicate email
    session.add(user5)
    
    session.commit()
except Exception as e:
    session.rollback()
    print(f"\nTransaction rolled back: {e}")

# Verify Eve was not added due to rollback
eve = session.query(User).filter(User.name == "Eve").first()
print(f"Eve in database: {eve is not None}")

print("\n=== Closing Session ===")
session.close()

# Clean up
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"\nDatabase file '{db_file}' removed")

