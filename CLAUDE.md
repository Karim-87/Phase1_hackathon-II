# Claude Code Rules

This file contains project-specific instructions for Claude Code when working on this project.

## Project Overview

This is a UV-based Python CLI Todo application that stores data in memory only. The entire application is implemented in a single file (src/main.py).

## Constraints

- All code must be in src/main.py (single-file constraint)
- No external storage - in-memory only
- Use Python 3.13+ standard library only
- Must run with: `uv run python src/main.py`
- Follow clean code principles and type hints

## Architecture

- Todo data model with id, title, description, and completed fields
- Global in-memory storage using Python lists
- Menu-driven CLI interface
- Function-based organization within single file

## Development Guidelines

- Maintain type hints throughout
- Implement proper input validation
- Follow error handling strategy (graceful handling, user-friendly messages)
- Keep functions focused and well-documented
- Preserve the in-memory only constraint
- Ensure CLI is user-friendly with clear prompts and messages