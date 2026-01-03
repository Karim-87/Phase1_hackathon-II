# Tasks: UV-based Python CLI Todo App

## Task List

### 1. Initialize UV Project
- **Description**: Set up the basic UV project structure
- **Steps**:
  - Run `uv init` to create project configuration
  - Configure pyproject.toml with Python 3.13+ requirement
  - Verify project structure is created correctly
- **Acceptance Criteria**:
  - Project directory contains pyproject.toml
  - pyproject.toml specifies Python 3.13+
  - Basic project structure is valid

### 2. Configure Python Version
- **Description**: Ensure project is configured for Python 3.13+
- **Steps**:
  - Update pyproject.toml to specify Python 3.13+ requirement
  - Verify compatibility with target Python version
- **Acceptance Criteria**:
  - pyproject.toml correctly specifies Python version requirement
  - Project can be built with specified Python version

### 3. Create src/main.py
- **Description**: Create the main application file
- **Steps**:
  - Create src directory
  - Create empty main.py file
  - Add basic file structure with imports
- **Acceptance Criteria**:
  - src directory exists
  - src/main.py file exists
  - Basic imports are included (typing, dataclasses, etc.)

### 4. Define In-Memory Task List
- **Description**: Set up the data structures for in-memory storage
- **Steps**:
  - Define global list variable for todos
  - Define Todo data class with id, title, description, completed fields
  - Initialize empty todos list
  - Define next_id counter
- **Acceptance Criteria**:
  - Todo data class is properly defined
  - Global todos list exists
  - ID counter is initialized

### 5. Implement Add Todo Function
- **Description**: Create function to add new todos
- **Steps**:
  - Implement add_todo() function with type hints
  - Generate unique ID for new todo
  - Add validation for title (non-empty)
  - Add new todo to the global list
  - Return the created todo
- **Acceptance Criteria**:
  - Function creates new todo with unique ID
  - Title validation works correctly
  - New todo is added to the list
  - Function has proper type hints

### 6. Implement List Todos Function
- **Description**: Create function to retrieve all todos
- **Steps**:
  - Implement list_todos() function with type hints
  - Return all todos from the global list
  - Format output appropriately
- **Acceptance Criteria**:
  - Function returns all todos
  - Return type is properly typed
  - Function works with empty list

### 7. Implement Update Todo Function
- **Description**: Create function to update existing todos
- **Steps**:
  - Implement update_todo() function with type hints
  - Find todo by ID
  - Update title and/or description if provided
  - Return success/failure status
- **Acceptance Criteria**:
  - Function updates existing todo by ID
  - Only updates provided fields
  - Returns success status
  - Handles invalid ID appropriately

### 8. Implement Delete Todo Function
- **Description**: Create function to delete todos by ID
- **Steps**:
  - Implement delete_todo() function with type hints
  - Find and remove todo by ID
  - Return success/failure status
- **Acceptance Criteria**:
  - Function removes todo by ID
  - Returns success status
  - Handles invalid ID appropriately

### 9. Implement Mark Complete/Incomplete Function
- **Description**: Create function to toggle completion status
- **Steps**:
  - Implement toggle_todo_status() function with type hints
  - Find todo by ID
  - Toggle the completed status
  - Return success/failure status
- **Acceptance Criteria**:
  - Function toggles completion status
  - Returns success status
  - Handles invalid ID appropriately

### 10. Implement CLI Menu Loop
- **Description**: Create the main menu interface loop
- **Steps**:
  - Implement display_menu() function
  - Create main() function with menu loop
  - Implement run_application() function
  - Add option handling for each menu choice
  - Format output for each operation
- **Acceptance Criteria**:
  - Menu displays correctly
  - Loop continues until exit option
  - Each menu option performs correct action
  - Application exits when requested

### 11. Add Input Validation
- **Description**: Implement validation for all user inputs
- **Steps**:
  - Create get_user_choice() function with validation
  - Create get_todo_id() function with validation
  - Add validation for title and description inputs
  - Implement error handling for invalid inputs
  - Add user-friendly error messages
- **Acceptance Criteria**:
  - All user inputs are validated
  - Invalid inputs are handled gracefully
  - Clear error messages are shown
  - Application doesn't crash on invalid input

### 12. Create README.md
- **Description**: Create project documentation file
- **Steps**:
  - Write project overview
  - Document setup instructions
  - Document usage instructions
  - Include example commands
- **Acceptance Criteria**:
  - README.md file exists
  - Contains clear setup instructions
  - Contains usage instructions
  - Includes example commands

### 13. Create CLAUDE.md
- **Description**: Create Claude Code instructions file
- **Steps**:
  - Document project-specific Claude Code rules
  - Include project constraints and guidelines
  - Add specific instructions for this project
- **Acceptance Criteria**:
  - CLAUDE.md file exists
  - Contains relevant project instructions
  - Follows Claude Code conventions