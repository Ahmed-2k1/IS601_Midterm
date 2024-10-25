"""
add.py

This module provides the Add class to handle addition operations in the calculator.
The result of the addition is displayed and saved to the calculation history.

Classes:
    Add - Executes addition and stores the result in the history.

Usage:
    from add import Add
"""

import logging
from app.commands import Command
from app.history_manager import HistoryManager
class Add(Command):
    """
    A command to perform addition between two numbers.

    Methods:
        execute() - Prompts for two numbers, adds them, displays the result, and stores it in history.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the addition operation by taking user input for two numbers, calculating the sum,
        and displaying and storing the result.

        Raises:
            ValueError: If the input is not a valid number.
        """

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            logging.info(f"Adding {num1} and {num2}: Result = {result}")
            print(f"The result of {num1} + {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Add", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for addition: {e}")
            print("Error: Please enter valid numbers.")
