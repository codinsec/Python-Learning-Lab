# Pip, Venv, and Poetry in Python

import subprocess
import sys
import os

print("=== Virtual Environment (venv) ===")

print("""
Creating a virtual environment:

Windows:
  python -m venv .venv
  .venv\\Scripts\\activate

Linux/Mac:
  python -m venv .venv
  source .venv/bin/activate

Deactivating:
  deactivate
""")

# Check if we're in a virtual environment
in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
print(f"Currently in virtual environment: {in_venv}")
if in_venv:
    print(f"Virtual environment path: {sys.prefix}")

print("\n=== Pip Package Management ===")

print("""
Common pip commands:

Install a package:
  pip install package_name

Install specific version:
  pip install package_name==1.2.3

Install from requirements file:
  pip install -r requirements.txt

List installed packages:
  pip list

Show package info:
  pip show package_name

Uninstall package:
  pip uninstall package_name

Freeze current packages:
  pip freeze > requirements.txt
""")

# Example requirements.txt content
requirements_content = """# Example requirements.txt
requests==2.31.0
flask==3.0.0
pytest==7.4.3
python-dotenv==1.0.0
"""

print("Example requirements.txt content:")
print(requirements_content)

print("\n=== Requirements File Structure ===")

# Simulate reading requirements
requirements = [
    "requests==2.31.0",
    "flask==3.0.0",
    "pytest>=7.0.0",
    "python-dotenv~=1.0.0"
]

print("Requirements with version specifiers:")
for req in requirements:
    print(f"  {req}")

print("""
Version specifiers:
  ==  : Exact version
  >=  : Minimum version
  <=  : Maximum version
  ~=  : Compatible release
  !=  : Exclude version
""")

print("\n=== Poetry Overview ===")

print("""
Poetry is a modern dependency management tool for Python.

Installation:
  pip install poetry

Initialize new project:
  poetry new project-name

Initialize in existing project:
  poetry init

Add dependency:
  poetry add package-name

Add development dependency:
  poetry add --dev pytest

Install dependencies:
  poetry install

Update dependencies:
  poetry update

Show installed packages:
  poetry show

Remove package:
  poetry remove package-name
""")

print("\n=== pyproject.toml Structure ===")

pyproject_toml_example = """[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "My Python project"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"
flask = "^3.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
black = "^23.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""

print("Example pyproject.toml:")
print(pyproject_toml_example)

print("\n=== Virtual Environment Best Practices ===")

best_practices = [
    "Always use virtual environments for projects",
    "Never install packages globally",
    "Keep requirements.txt or pyproject.toml updated",
    "Use specific versions in production",
    "Document dependencies clearly",
    "Use .gitignore to exclude .venv/",
    "Create separate environments for different projects"
]

print("Best practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

print("\n=== Checking Installed Packages ===")

try:
    # Try to get pip list (if available)
    result = subprocess.run([sys.executable, "-m", "pip", "list"], 
                          capture_output=True, text=True, timeout=5)
    if result.returncode == 0:
        lines = result.stdout.split('\n')[:10]  # First 10 lines
        print("Sample of installed packages:")
        for line in lines:
            if line.strip():
                print(f"  {line}")
    else:
        print("Could not retrieve package list")
except Exception as e:
    print(f"Note: Package listing requires pip to be available")
    print(f"Error: {e}")

print("\n=== Environment Variables for Python Path ===")

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path[:3]}...")  # First 3 entries

print("\n=== Creating Requirements File Programmatically ===")

def create_requirements_file(packages, filename="requirements.txt"):
    """Example function to create requirements file"""
    with open(filename, "w") as f:
        for package in packages:
            f.write(f"{package}\n")
    print(f"Created {filename} with {len(packages)} packages")

# Example usage (commented out to avoid creating file)
# packages = ["requests==2.31.0", "flask==3.0.0"]
# create_requirements_file(packages)

print("\n=== Dependency Management Workflow ===")

workflow_steps = [
    "1. Create virtual environment: python -m venv .venv",
    "2. Activate virtual environment",
    "3. Install packages: pip install package-name",
    "4. Freeze dependencies: pip freeze > requirements.txt",
    "5. Commit requirements.txt to version control",
    "6. Others can install: pip install -r requirements.txt"
]

print("Typical workflow:")
for step in workflow_steps:
    print(f"  {step}")

print("\n=== Poetry vs Pip/Venv ===")

comparison = {
    "Pip + Venv": [
        "Standard Python tooling",
        "Simple and straightforward",
        "Manual dependency resolution",
        "requirements.txt for dependencies"
    ],
    "Poetry": [
        "Modern dependency management",
        "Automatic dependency resolution",
        "Lock file for reproducible builds",
        "Integrated build and publish tools",
        "pyproject.toml for configuration"
    ]
}

for tool, features in comparison.items():
    print(f"\n{tool}:")
    for feature in features:
        print(f"  - {feature}")

