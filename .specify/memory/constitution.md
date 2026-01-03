<!--
Sync Impact Report:
Version change: 1.0.0 → 1.1.0
Added sections: Project Name, Primary Goal, Environment Rules, Technical Constraints, Functional Requirements, Architecture Rules, Folder Structure, Development Process
Removed sections: None
Modified principles: All 6 principles redefined for Todo CLI application
Templates requiring updates: ✅ Updated
Follow-up TODOs: None
-->

# In-Memory Todo CLI Application Constitution

## Core Principles

### I. In-Memory Architecture
The application stores all data in memory only with no persistent storage. No files, databases, or external storage systems may be used. This ensures simplicity and prevents data persistence across application runs. Rationale: Maintains the clean, stateless nature of the application while focusing on core functionality.

### II. Command-Line Interface Focus
All user interactions occur through a console-based interface. The application must accept command-line arguments and provide clear, readable output to stdout/stderr. Input validation and user-friendly error messages are required. Rationale: Provides a lightweight, efficient interface that works in any terminal environment.

### III. UV Package Management (NON-NEGOTIABLE)
UV must be used for all dependency management and project execution. All commands must be compatible with UV, and the project must run using `uv run python src/main.py`. This ensures consistent, fast package management. Rationale: Maintains consistency and leverages UV's performance advantages.

### IV. Type Safety and Clean Code
All code must use type hints and follow PEP8 standards. Functions should have clear, single responsibilities with well-defined boundaries. Code must be modular, testable, and maintainable. Rationale: Ensures code quality, readability, and maintainability.

### V. Python 3.13+ Standard Library Only
The application must use only Python 3.13+ standard library modules with no external dependencies beyond what UV manages for the project structure. No third-party packages for core functionality. Rationale: Ensures portability and reduces external dependencies.

### VI. Test-Driven Development
All features must be developed using TDD: tests written first, then implementation. Each function and feature must have corresponding unit tests. The Red-Green-Refactor cycle must be strictly followed. Rationale: Ensures code reliability and prevents regressions.

## Technical Constraints and Requirements

- Python version: 3.13+
- In-memory storage only (no files, no database)
- Console-based interaction
- Standard Python library only
- UV for project management
- Project must run using `uv run python src/main.py`

## Functional Requirements

1. Add todo with title and description
2. List all todos with ID and status
3. Update todo by ID
4. Delete todo by ID
5. Mark todo complete/incomplete

## Architecture Rules

- Clean code principles
- Separation of concerns
- Modular design
- Use type hints throughout
- Single responsibility for functions
- Clear input/output boundaries

## Folder Structure

- /src - Main source code
- /specs/history - Specification files
- README.md - Project documentation
- CLAUDE.md - Claude Code instructions

## Development Process

- Use Spec-Kit Plus commands only
- Follow order: specify → plan → tasks → implement
- Store all specs in specs/history
- All changes must follow the Agentic Dev Stack workflow
- Each task must be testable and verifiable

## Governance

This constitution supersedes all other development practices. All code reviews must verify compliance with these principles. Any architectural decisions that conflict with these principles require constitution amendments. All pull requests must demonstrate adherence to these rules.

**Version**: 1.1.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
