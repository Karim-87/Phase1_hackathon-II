#!/usr/bin/env python3
"""
CLI Todo Application

A command-line Todo application that stores data in memory only.
Features include adding, listing, updating, deleting, and marking todos as complete.
"""

from typing import Dict, List, Optional, Union
import sys


class Todo:
    """Represents a single todo item."""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        """Convert the todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def __str__(self) -> str:
        """String representation of the todo."""
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}. {self.title} - {self.description}"


# Global in-memory storage
todos: List[Todo] = []
next_id: int = 1


def add_todo(title: str, description: str = "") -> Optional[Todo]:
    """
    Add a new todo to the list.

    Args:
        title: The title of the todo (required)
        description: The description of the todo (optional)

    Returns:
        The created Todo object or None if invalid input
    """
    global next_id

    if not title or not title.strip():
        print("Error: Title cannot be empty.")
        return None

    if len(title) > 500:
        print("Error: Title is too long (max 500 characters).")
        return None

    if len(description) > 2000:
        print("Error: Description is too long (max 2000 characters).")
        return None

    todo = Todo(id=next_id, title=title.strip(), description=description.strip())
    todos.append(todo)
    next_id += 1

    print(f"Successfully added todo with ID {todo.id}")
    return todo


def list_todos() -> List[Todo]:
    """
    List all todos.

    Returns:
        List of all Todo objects
    """
    if not todos:
        print("No todos found.")
        return []

    print("\nYour Todos:")
    print("-" * 50)
    for todo in todos:
        print(todo)
    print("-" * 50)

    return todos


def get_todo(todo_id: int) -> Optional[Todo]:
    """
    Get a specific todo by ID.

    Args:
        todo_id: The ID of the todo to retrieve

    Returns:
        The Todo object if found, None otherwise
    """
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


def update_todo(todo_id: int, title: str = None, description: str = None) -> bool:
    """
    Update an existing todo.

    Args:
        todo_id: The ID of the todo to update
        title: New title (optional)
        description: New description (optional)

    Returns:
        True if update was successful, False otherwise
    """
    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return False

    if title is not None:
        if not title.strip():
            print("Error: Title cannot be empty.")
            return False
        if len(title) > 500:
            print("Error: Title is too long (max 500 characters).")
            return False
        todo.title = title.strip()

    if description is not None:
        if len(description) > 2000:
            print("Error: Description is too long (max 2000 characters).")
            return False
        todo.description = description.strip()

    print(f"Successfully updated todo with ID {todo_id}")
    return True


def delete_todo(todo_id: int) -> bool:
    """
    Delete a todo by ID.

    Args:
        todo_id: The ID of the todo to delete

    Returns:
        True if deletion was successful, False otherwise
    """
    global todos

    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return False

    todos = [t for t in todos if t.id != todo_id]
    print(f"Successfully deleted todo with ID {todo_id}")
    return True


def toggle_todo_status(todo_id: int) -> bool:
    """
    Toggle the completion status of a todo.

    Args:
        todo_id: The ID of the todo to toggle

    Returns:
        True if toggle was successful, False otherwise
    """
    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return False

    todo.completed = not todo.completed
    status = "completed" if todo.completed else "incomplete"
    print(f"Todo with ID {todo_id} marked as {status}")
    return True


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("CLI Todo Application")
    print("="*40)
    print("1. Add Todo")
    print("2. List Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Mark Todo Complete/Incomplete")
    print("6. Exit")
    print("-"*40)


def get_user_choice() -> int:
    """
    Get and validate user menu choice.

    Returns:
        Valid menu choice (1-6)
    """
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= 6:
                return choice_num
            else:
                print("Error: Please enter a number between 1 and 6.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_todo_id() -> int:
    """
    Get and validate todo ID from user.

    Returns:
        Valid todo ID
    """
    while True:
        try:
            todo_id = input("Enter todo ID: ").strip()
            id_num = int(todo_id)
            if id_num > 0:
                return id_num
            else:
                print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Please enter a valid number.")


def handle_add_todo():
    """Handle the add todo flow."""
    print("\n--- Add New Todo ---")
    title = input("Enter title: ").strip()

    if not title:
        print("Error: Title cannot be empty.")
        return

    description = input("Enter description (optional): ").strip()

    add_todo(title, description)


def handle_list_todos():
    """Handle the list todos flow."""
    print("\n--- All Todos ---")
    list_todos()


def handle_update_todo():
    """Handle the update todo flow."""
    print("\n--- Update Todo ---")
    todo_id = get_todo_id()

    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return

    print(f"Current todo: {todo}")

    new_title = input(f"Enter new title (current: '{todo.title}', press Enter to keep): ").strip()
    new_description = input(f"Enter new description (current: '{todo.description}', press Enter to keep): ").strip()

    # Use None to indicate no change, empty string to clear
    title_to_update = new_title if new_title != "" else (todo.title if new_title == "" else None)
    description_to_update = new_description if new_description != "" else (todo.description if new_description == "" else None)

    update_todo(todo_id, title_to_update if new_title != "" else None,
                description_to_update if new_description != "" else None)


def handle_delete_todo():
    """Handle the delete todo flow."""
    print("\n--- Delete Todo ---")
    todo_id = get_todo_id()

    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return

    print(f"Todo to delete: {todo}")

    confirm = input("Are you sure you want to delete this todo? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        delete_todo(todo_id)
    else:
        print("Deletion cancelled.")


def handle_toggle_todo():
    """Handle the toggle todo status flow."""
    print("\n--- Toggle Todo Status ---")
    todo_id = get_todo_id()

    todo = get_todo(todo_id)
    if not todo:
        print(f"Error: Todo with ID {todo_id} not found.")
        return

    print(f"Current status: {'Completed' if todo.completed else 'Incomplete'}")
    toggle_todo_status(todo_id)


def run_application():
    """Run the main application loop."""
    print("Welcome to the CLI Todo Application!")
    print("This application stores all data in memory only.")
    print("Data will be lost when the application exits.")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_add_todo()
        elif choice == 2:
            handle_list_todos()
        elif choice == 3:
            handle_update_todo()
        elif choice == 4:
            handle_delete_todo()
        elif choice == 5:
            handle_toggle_todo()
        elif choice == 6:
            print("Thank you for using the CLI Todo Application. Goodbye!")
            break


def main():
    """Main function to run the application."""
    try:
        run_application()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()