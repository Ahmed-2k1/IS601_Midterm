
# IS601 Midterm Advanced Calculator

## Overview

This project is a command-line calculator built in Python, designed with modularity in mind. It allows basic arithmetic operations, records and retrieves calculation history, and supports extensible features through a plugin system. The architecture incorporates several design patterns, including Command, Facade, Singleton, and Plugin-based designs.

## Key Features

- **Arithmetic Functions**: Supports essential operations such as addition, subtraction, multiplication, and division.
- **History Management**: Saves and loads calculation history via a CSV file with the help of Pandas.
- **Command Pattern**: Enables consistent execution of commands.
- **Comprehensive Logging**: Captures details on command usage and errors for troubleshooting.
- **Environment Variable Configuration**: Allows dynamic configuration adjustments.
- **Plugin Support**: Easily add or remove features.

## Design Patterns

### 1. Command Pattern

The **Command Pattern** allows each function to be encapsulated as a standalone command class. Commands like `add`, `subtract`, and `save_history` use this pattern, standardizing their execution.

- **Why Command Pattern?** It simplifies the addition of new functions and maintains the structure of the application.
- **Code Examples**:
  - [Addition Command](app/plugins/calculator/add.py)
  - [Subtraction Command](app/plugins/calculator/subtract.py)
  - [History Commands](app/plugins/calculator/history_commands.py)

### 2. Facade Pattern

The **Facade Pattern** in `history_manager.py` simplifies interaction with the history management system. It provides methods to save, load, clear, and delete records, minimizing complexity for the user.

- **Why Facade Pattern?** It provides a simpler interface for history management functions, making interactions straightforward.
- **Code Example**:
  - [History Manager](app/history_manager.py)

### 3. Singleton Pattern

The **Singleton Pattern** guarantees that certain configurations, such as logging, have a single instance across the application.

- **Why Singleton Pattern?** It ensures configuration consistency by allowing only one instance for setup details.
- **Code Example**:
  - [Logging Setup](logging.conf)

### 4. Plugin Architecture

The **Plugin Architecture** enables adding new features (e.g., `greet`, `calculator`, `menu`, `exit`) dynamically by creating new plugin modules.

- **Why Plugin Architecture?** It allows flexibility, making it easy to add or remove commands without modifying the main code.
- **Code Examples**:
  - [Calculator Plugins](app/plugins/calculator/)
  - [Greet Plugin](app/plugins/greet/__init__.py)
  - [Menu Plugin](app/plugins/menu/__init__.py)
  - [Exit Plugin](app/plugins/exit/__init__.py)

## Environment Variables

Environment variables provide flexible configuration, managing settings such as the history file location or logging paths. This flexibility allows the application to adapt to different deployment setups.

- **Code Reference**: Environment variables are set up within [main.py](main.py).

## Logging

Logging is configured in `logging.conf`, which captures various logging levels like INFO, DEBUG, and ERROR. Logging is vital for tracking the application's actions and identifying issues.

- **Logging Highlights**:
  - **Commands**: Records each command executed by the user.
  - **Error Handling**: Logs exceptions, aiding in debugging.
  - **History Management**: Logs operations related to saving, loading, and clearing history.

- **Code Reference**:
  - [Logging Config](logging.conf)

## Error Handling: LBYL and EAFP

This project employs **Look Before You Leap (LBYL)** by checking conditions (e.g., validating file paths or index ranges) before proceeding. **Easier to Ask for Forgiveness than Permission (EAFP)** could be implemented with `try-except` blocks to manage errors more fluidly.

- **Code Examples**:
  - **LBYL**: File checks in [history_manager.py](app/history_manager.py)
  - **EAFP**: Could be added in future updates to handle file access and similar tasks.


## Usage

Start the application from the command line:

```bash
python main.py
```

### Commands

In the REPL interface, available commands include:

- **Calculator Commands**:
  - `add <num1> <num2>`
  - `subtract <num1> <num2>`
  - `multiply <num1> <num2>`
  - `divide <num1> <num2>`
- **History Commands**:
  - `save`, `load`, `clear`, `delete <index>`
- **General Commands**:
  - `greet`, `menu`, `exit`

## Testing

A comprehensive test suite in the `tests` directory covers all components. Run tests with:

```bash
pytest
```

## CI/CD

GitHub Actions are used for automated testing, ensuring consistent code quality with each update.

## Video Link
https://drive.google.com/file/d/1p0nnWdmV7gme9OWBlj2BvVTY2OPCm9yI/view?usp=sharing  
