# Todo CLI Application Specification

## Project Overview

A command-line Todo application built with Python that provides users with a simple interface to manage their tasks. The application runs within a UV-managed project environment and stores all data in memory only, with no persistent storage. Users can add, view, update, delete, and mark todos as complete/incomplete through a menu-driven interface.

## UV-based Project Setup Explanation

The project utilizes UV as the package manager and project runner. UV provides fast, reliable dependency management and project execution. The application will be structured to run with the command `uv run python src/main.py`. UV handles virtual environment management, dependency resolution, and ensures consistent Python runtime behavior across different environments.

## Python Version Requirements

The application requires Python 3.13 or higher. This ensures access to the latest Python features and security updates while maintaining compatibility with modern development practices. The project will leverage Python's standard library only, with no external dependencies beyond what UV manages for the project structure.

## CLI User Interaction Flow

The application presents a menu-driven interface that repeatedly displays options to the user until they choose to exit. The interface accepts numeric input to select menu options and validates all user input to prevent errors. After each operation, the application returns to the main menu to allow continued interaction. The interface provides clear, user-friendly messages for both success and error conditions.

## Todo Features and Commands

The application provides the following core features:

1. **Add Todo**: Allows users to create new todo items with a title and optional description
2. **List Todos**: Displays all todos with their ID, title, description, and completion status
3. **Update Todo**: Enables users to modify the title and description of existing todos by ID
4. **Delete Todo**: Allows users to remove todos by ID with confirmation
5. **Mark Todo Complete/Incomplete**: Toggles the completion status of a todo by ID
6. **Exit**: Terminates the application

## In-Memory Data Model

The application uses Python data structures to maintain todos in memory only. The data model includes:

- **Todo Entity**:
  - `id`: integer (unique identifier)
  - `title`: string (required task title)
  - `description`: string (optional task description)
  - `completed`: boolean (completion status, defaults to False)

The data is stored in a Python list and will be lost when the application terminates. This ensures simplicity and focuses on core functionality without the complexity of persistent storage.

## Error Handling Rules

The application implements comprehensive error handling to ensure a smooth user experience:

- All user inputs are validated before processing
- Invalid numeric inputs result in clear error messages and prompt for re-entry
- Attempts to access non-existent todo IDs result in appropriate error messages
- Empty or invalid titles are rejected with clear feedback
- The application never crashes due to user input errors
- All error messages are descriptive and guide users toward correct usage

## Constraints and Assumptions

- **No Persistent Storage**: Data exists only in memory and is lost when the application exits
- **Single User**: The application is designed for a single user at a time
- **Console Interface**: All interaction occurs through the command line
- **Standard Library Only**: No external dependencies beyond UV project management
- **Integer IDs**: Todo IDs are assigned sequentially as integers starting from 1
- **Python 3.13+**: The application requires Python 3.13 or higher
- **UV Runtime**: The application must run using `uv run python src/main.py`

## Success Criteria

- Users can successfully add, view, update, delete, and mark todos as complete/incomplete
- The application handles all user input validation without crashing
- All operations complete within a reasonable time frame (less than 1 second for typical operations)
- The menu interface is intuitive and provides clear feedback for all actions
- Error conditions are handled gracefully with user-friendly messages
- The application maintains data integrity during all operations

## Assumptions

- Users have basic command-line interface familiarity
- The Python 3.13+ and UV environments are properly configured
- Users will enter reasonable input lengths (titles/descriptions under 1000 characters)
- The application will handle a reasonable number of todos (up to 1000 items) without performance issues