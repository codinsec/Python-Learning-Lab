# Migrations with Alembic

print("=== What are Database Migrations? ===")

print("""
Database migrations are a way to version control your database schema.
They allow you to:
- Track changes to database structure over time
- Apply changes consistently across environments
- Rollback changes if needed
- Collaborate on database changes with your team
""")

print("\n=== Alembic Overview ===")

print("""
Alembic is SQLAlchemy's database migration tool.

Key concepts:
- Migration: A script that describes a change to the database
- Revision: A unique identifier for a migration
- Upgrade: Apply a migration (forward)
- Downgrade: Rollback a migration (backward)
- Head: The latest migration
""")

print("\n=== Alembic Installation ===")

print("""
Install Alembic:
  pip install alembic

Or with SQLAlchemy:
  pip install alembic sqlalchemy
""")

print("\n=== Initial Setup ===")

print("""
1. Initialize Alembic in your project:
   alembic init alembic

This creates:
  - alembic/ directory (migration scripts)
  - alembic.ini (configuration file)
  - alembic/env.py (environment setup)
  - alembic/script.py.mako (migration template)
""")

print("\n=== Configuration (alembic.ini) ===")

alembic_ini_example = """
# alembic.ini example

[alembic]
script_location = alembic

# Database URL
sqlalchemy.url = sqlite:///example.db

# Template for migration files
file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
"""

print("Example alembic.ini configuration:")
print(alembic_ini_example)

print("\n=== Environment Setup (alembic/env.py) ===")

env_py_example = """
# alembic/env.py example

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from myapp.models import Base  # Import your models

# Set target metadata
target_metadata = Base.metadata

# Get database URL from config
config = context.config
if config.get_main_option("sqlalchemy.url"):
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
"""

print("Example env.py setup:")
print(env_py_example)

print("\n=== Creating Migrations ===")

print("""
1. Create initial migration (if starting fresh):
   alembic revision --autogenerate -m "Initial migration"

2. Create migration for model changes:
   alembic revision --autogenerate -m "Add user table"

3. Create empty migration (manual):
   alembic revision -m "Custom migration"
""")

print("\n=== Migration File Structure ===")

migration_example = """
# Migration file example: 001_add_users_table.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Apply this migration
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Rollback this migration
    op.drop_table('users')
"""

print("Example migration file:")
print(migration_example)

print("\n=== Common Migration Operations ===")

operations = {
    "Create Table": "op.create_table('table_name', ...)",
    "Drop Table": "op.drop_table('table_name')",
    "Add Column": "op.add_column('table_name', sa.Column('col_name', sa.String()))",
    "Drop Column": "op.drop_column('table_name', 'col_name')",
    "Alter Column": "op.alter_column('table_name', 'col_name', type_=sa.String(100))",
    "Create Index": "op.create_index('idx_name', 'table_name', ['column'])",
    "Drop Index": "op.drop_index('idx_name', 'table_name')"
}

print("Common operations:")
for operation, code in operations.items():
    print(f"  {operation}: {code}")

print("\n=== Applying Migrations ===")

print("""
Apply all pending migrations:
  alembic upgrade head

Apply to specific revision:
  alembic upgrade <revision_id>

Apply one migration:
  alembic upgrade +1
""")

print("\n=== Rolling Back Migrations ===")

print("""
Rollback one migration:
  alembic downgrade -1

Rollback to specific revision:
  alembic downgrade <revision_id>

Rollback all migrations:
  alembic downgrade base
""")

print("\n=== Checking Migration Status ===")

print("""
Check current migration status:
  alembic current

View migration history:
  alembic history

View pending migrations:
  alembic heads
""")

print("\n=== Migration Workflow ===")

workflow_steps = [
    "1. Make changes to your SQLAlchemy models",
    "2. Generate migration: alembic revision --autogenerate -m 'description'",
    "3. Review the generated migration file",
    "4. Apply migration: alembic upgrade head",
    "5. Test your application",
    "6. Commit migration files to version control"
]

print("Typical workflow:")
for step in workflow_steps:
    print(f"  {step}")

print("\n=== Handling Migration Conflicts ===")

print("""
If migrations conflict:
1. Check current state: alembic current
2. View history: alembic history
3. Resolve conflicts manually in migration files
4. Stamp database to specific revision if needed:
   alembic stamp <revision_id>
""")

print("\n=== Best Practices ===")

best_practices = [
    "Always review auto-generated migrations before applying",
    "Test migrations on development database first",
    "Keep migrations small and focused",
    "Never edit applied migrations (create new ones instead)",
    "Use descriptive migration messages",
    "Backup database before applying migrations in production",
    "Version control all migration files",
    "Keep migrations reversible (implement downgrade)"
]

print("Migration best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Example: Adding a Column ===")

add_column_example = """
# Migration: Add age column to users table

def upgrade():
    op.add_column('users', 
        sa.Column('age', sa.Integer(), nullable=True)
    )

def downgrade():
    op.drop_column('users', 'age')
"""

print("Example migration - adding a column:")
print(add_column_example)

print("\n=== Example: Creating Relationship ===")

relationship_example = """
# Migration: Add foreign key for posts table

def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('posts')
"""

print("Example migration - creating relationship:")
print(relationship_example)

print("\n=== Environment-Specific Configuration ===")

print("""
For different environments, you can:

1. Use environment variables in alembic.ini:
   sqlalchemy.url = ${DATABASE_URL}

2. Or override in env.py:
   import os
   config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))
""")

print("\n=== Migration Script Template ===")

template_info = """
Alembic uses script.py.mako as template for new migrations.

You can customize it to include:
- Your project's imports
- Common patterns
- Custom functions
"""

print(template_info)

