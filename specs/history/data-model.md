# Data Model: UV-based Python CLI Todo App

## Todo Entity

### Fields
- **id**: integer
  - Type: int
  - Constraints: Unique, auto-incrementing, positive integer
  - Required: Yes
  - Description: Unique identifier for each todo item

- **title**: string
  - Type: str
  - Constraints: Non-empty, max 500 characters
  - Required: Yes
  - Description: Brief description of the todo task

- **description**: string
  - Type: str
  - Constraints: Optional, max 2000 characters
  - Required: No
  - Description: Detailed information about the todo task

- **completed**: boolean
  - Type: bool
  - Constraints: True or False
  - Required: Yes
  - Default: False
  - Description: Completion status of the todo task

### Validation Rules
1. Title must be a non-empty string (1-500 characters)
2. Description can be empty but must be a string if provided (0-2000 characters)
3. ID must be unique within the application session
4. Completed status must be a boolean value
5. ID must be a positive integer

### State Transitions
- Creation: `completed` defaults to False
- Update: `completed` can be toggled between True and False
- Deletion: Todo is removed from the in-memory list

## Data Storage Structure

### In-Memory Storage
- **Type**: List[Dict[str, Union[int, str, bool]]]
- **Name**: `todos`
- **Description**: List of todo dictionaries stored in memory
- **Access**: Global variable accessible by all functions

### ID Generation
- **Type**: int
- **Name**: `next_id`
- **Description**: Tracks the next available ID for new todos
- **Initial Value**: 1
- **Increment**: Increases by 1 for each new todo added

## Relationships
- No relationships exist as this is a single-entity application
- Each todo is independent of others
- All todos are stored in the same in-memory list