# CLI Todo Application

A command-line Todo application built with Python that runs inside a UV-managed project. The application stores all data in memory only, with no persistent storage.

## Features

- Add new todos with title and description
- List all todos with their status
- Update existing todos by ID
- Delete todos by ID
- Mark todos as complete/incomplete
- In-memory storage (data is lost when application exits)

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

1. Install UV if you haven't already:
   ```bash
   pip install uv
   ```

2. Install project dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the application with:
```bash
uv run python src/main.py
```

The application will present a menu-driven interface where you can:
1. Add Todo - Create new todo items
2. List Todos - View all existing todos
3. Update Todo - Modify existing todos by ID
4. Delete Todo - Remove todos by ID
5. Mark Todo Complete/Incomplete - Toggle completion status
6. Exit - Quit the application

## Data Model

Each todo contains:
- ID: Unique integer identifier
- Title: Required string (non-empty)
- Description: Optional string
- Completed: Boolean status (default: False)

## Architecture

- Single-file implementation in `src/main.py`
- In-memory data storage using Python lists and objects
- Menu-driven CLI interface
- Input validation for all user inputs
- Error handling for invalid operations