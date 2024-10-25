"""
multiply.py

This module provides the Multiply class to handle multiplication operations in the calculator.
The result of the multiplication is displayed and saved to the calculation history.

Classes:
    Multiply - Executes multiplication and stores the result in the history.

Usage:
    from multiply import Multiply
"""

import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Multiply(Command):
    """
    A command to perform multiplication between two numbers.

    Methods:
        execute() - Prompts for two numbers, multiplies them, displays the result, and stores it in history.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the multiplication operation by taking user input for two numbers, calculating the product,
        and displaying and storing the result.

        Raises:
            ValueError: If the input is not a valid number.
        """
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            logging.info(f"Multiplying {num1} and {num2}: Result = {result}")
            print(f"The result of {num1} * {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Multiply", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for multiplication: {e}")
            print("Error: Please enter valid numbers.")
            