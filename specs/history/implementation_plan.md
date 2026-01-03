# Implementation Plan: UV-based Python CLI Todo App

## Technical Context

**Feature**: Command-line Todo application with in-memory storage
**Architecture**: Single-file Python application (main.py)
**Runtime**: UV-managed project
**Target**: Python 3.13+
**Constraints**: Single file implementation, in-memory data, CLI interface

## Constitution Check

- ✅ In-Memory Architecture: Data stored in Python data structures only, no files/databases
- ✅ Command-Line Interface Focus: Menu-driven console interface with numeric input
- ✅ UV Package Management: Project setup with UV for dependency management
- ✅ Type Safety and Clean Code: Type hints and PEP8 standards followed
- ✅ Python 3.13+ Standard Library Only: No external dependencies beyond UV
- ✅ Test-Driven Development: Implementation will follow TDD principles

## Phase 0: Research

### UV Project Initialization
- Decision: Use `uv init` command to create project structure
- Rationale: Standard UV command creates proper project configuration
- Alternatives considered: Manual pyproject.toml creation (rejected as less standard)

### Single-File Architecture
- Decision: Implement all functionality in src/main.py
- Rationale: Meets constraint while maintaining code organization through functions
- Alternatives considered: Multiple modules (rejected due to single-file constraint)

## Phase 1: Data Model

### Todo Entity
- `id`: integer (auto-incrementing unique identifier)
- `title`: string (required, non-empty)
- `description`: string (optional, can be empty)
- `completed`: boolean (default False)

### Validation Rules
- Title must be non-empty string
- ID must be unique within the application session
- Description can be empty but not None

## Phase 2: Implementation Plan

### UV Project Setup
1. Initialize UV project with `uv init`
2. Configure for Python 3.13+
3. Set up src directory structure
4. Verify project runs with `uv run python src/main.py`

### src Folder Setup
- Create `src/` directory
- Create `src/main.py` as single application file
- Ensure proper module structure for UV execution

### Function-Level Breakdown (src/main.py)

#### Core Data Structures
- `todos`: List[Dict] - in-memory storage for todo items
- `next_id`: integer - auto-incrementing ID counter

#### Core Functions
- `add_todo(title: str, description: str = "") -> Dict` - Create new todo
- `list_todos() -> List[Dict]` - Retrieve all todos
- `get_todo(todo_id: int) -> Optional[Dict]` - Get specific todo by ID
- `update_todo(todo_id: int, title: str = None, description: str = None) -> bool` - Update todo
- `delete_todo(todo_id: int) -> bool` - Delete todo by ID
- `toggle_todo_status(todo_id: int) -> bool` - Toggle completion status

#### CLI Interface Functions
- `display_menu()` - Show available options to user
- `handle_add_todo()` - Handle add todo flow with user input
- `handle_list_todos()` - Display all todos in formatted way
- `handle_update_todo()` - Handle update todo flow with user input
- `handle_delete_todo()` - Handle delete todo flow with confirmation
- `handle_toggle_todo()` - Handle toggle completion flow
- `get_user_choice() -> int` - Get and validate user menu choice
- `get_todo_id() -> int` - Get and validate todo ID from user

#### Main Application Flow
- `main()` - Main function that runs the menu loop
- `run_application()` - Application loop that displays menu and handles choices

### CLI Menu Loop Logic
1. Display numbered menu options:
   - 1. Add Todo
   - 2. List Todos
   - 3. Update Todo
   - 4. Delete Todo
   - 5. Mark Todo Complete/Incomplete
   - 6. Exit
2. Get user choice with validation
3. Execute corresponding function
4. Return to menu after operation
5. Exit only when user selects option 6

### In-Memory Task Handling Approach
- Use a global list variable to store todos during application runtime
- Implement functions to manipulate the list safely
- Use integer IDs for unique identification
- Implement proper error handling for invalid IDs
- Track next available ID to ensure uniqueness

### Error Handling Strategy
- Input validation for all user inputs
- Try-catch blocks for potential errors
- User-friendly error messages
- Continue execution after errors (don't crash)
- Validate todo IDs exist before operations
- Handle empty input for required fields

### Execution Flow
1. Initialize global data structures
2. Start main application loop
3. Display menu
4. Get user choice
5. Execute selected function
6. Handle errors gracefully
7. Return to menu or exit
8. Clean exit when requested

## Technology Stack
- Python 3.13+
- UV package manager
- Python standard library only

## Implementation Steps
1. Set up UV project structure
2. Create src/main.py file
3. Implement data structures and storage
4. Implement core todo functions
5. Implement CLI interface functions
6. Implement main application loop
7. Add error handling
8. Test functionality
9. Refactor for clean code principles