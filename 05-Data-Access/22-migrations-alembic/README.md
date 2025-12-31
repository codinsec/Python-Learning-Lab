# Migrations with Alembic

## Overview
This topic covers database migrations using Alembic, SQLAlchemy's migration tool. Learn how to version control database schema changes, create migrations, and apply them to keep databases in sync with code changes.

## Learning Objectives
- Understand database migrations and their importance
- Install and configure Alembic
- Create initial migration
- Generate migrations from model changes
- Apply and rollback migrations
- Work with migration scripts
- Handle migration conflicts

## Topics Covered
- Alembic installation and setup
- Initial migration creation
- Generating migrations
- Applying migrations (upgrade)
- Rolling back migrations (downgrade)
- Migration scripts structure
- Best practices for migrations

## How to Run
```bash
# Setup Alembic (first time)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

**Note:** Requires Alembic: `pip install alembic`

## Examples
The `main.py` file contains conceptual examples and explanations of Alembic usage patterns.

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

