# CLI Interface Contract: UV-based Python CLI Todo App

## Overview
This document defines the interface contract for the Todo CLI application. It specifies the expected behavior of the command-line interface and the data contracts for all operations.

## CLI Commands and Options

### Main Menu Options
The application presents a numbered menu with the following options:

1. **Add Todo**
   - Input: User provides title and optional description
   - Output: Success message with new todo ID
   - Error: Validation error if title is empty

2. **List Todos**
   - Input: None
   - Output: Formatted list of all todos with ID, title, description, and completion status
   - Error: None

3. **Update Todo**
   - Input: User provides todo ID and new title/description values
   - Output: Success message confirming update
   - Error: Error if todo ID doesn't exist or invalid input

4. **Delete Todo**
   - Input: User provides todo ID
   - Output: Success message confirming deletion
   - Error: Error if todo ID doesn't exist

5. **Mark Todo Complete/Incomplete**
   - Input: User provides todo ID
   - Output: Success message with new status
   - Error: Error if todo ID doesn't exist

6. **Exit**
   - Input: None
   - Output: Application termination

## Data Contracts

### Todo Object
```
{
  "id": integer,
  "title": string,
  "description": string,
  "completed": boolean
}
```

### Input Validation
- ID: Positive integer only
- Title: Non-empty string, max 500 characters
- Description: Optional string, max 2000 characters
- Completed: Boolean value only

### Error Responses
All errors follow the format:
```
{
  "error": "descriptive error message"
}
```

## User Interaction Flow
1. Application starts and displays menu
2. User selects option (1-6)
3. Application processes request
4. Application displays result or error
5. Application returns to main menu
6. Loop continues until user selects Exit

## Exit Conditions
- User selects option 6 (Exit)
- User sends interrupt signal (Ctrl+C)