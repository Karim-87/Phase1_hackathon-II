# Quickstart Guide: UV-based Python CLI Todo App

## Prerequisites
- Python 3.13 or higher
- UV package manager installed

## Setup Instructions

1. **Initialize the project**
   ```bash
   uv init
   ```

2. **Create the directory structure**
   ```bash
   mkdir src
   touch src/main.py
   ```

3. **Verify UV configuration**
   - Ensure pyproject.toml specifies Python 3.13+
   - Verify that the project is set up for execution

4. **Run the application**
   ```bash
   uv run python src/main.py
   ```

## Running the Application

The application will start with a menu interface that allows you to:
- Add new todos with title and description
- List all existing todos with their status
- Update existing todos
- Delete todos by ID
- Mark todos as complete/incomplete
- Exit the application

## Development Workflow

1. Make changes to src/main.py
2. Test with `uv run python src/main.py`
3. Verify all functionality works as expected
4. Commit changes when satisfied

## Troubleshooting

- If UV is not installed: Install with `pip install uv`
- If Python 3.13+ is not available: Install the latest Python version
- If the application fails to run: Verify the pyproject.toml configuration