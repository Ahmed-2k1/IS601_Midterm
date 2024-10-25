"""
subtract.py

This module provides the Subtract class to handle subtraction operations in the calculator.
The result of the subtraction is displayed and saved to the calculation history.

Classes:
    Subtract - Executes subtraction and stores the result in the history.

Usage:
    from subtract import Subtract
"""

import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Subtract(Command):
    """
    A command to perform subtraction between two numbers.

    Methods:
        execute() - Prompts for two numbers, subtracts them, displays the result, and stores it in history.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the subtraction operation by taking user input for two numbers, calculating the difference,
        and displaying and storing the result.

        Raises:
            ValueError: If the input is not a valid number.
        """
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            logging.info(f"Subtracting {num2} from {num1}: Result = {result}")
            print(f"The result of {num1} - {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Subtract", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for subtraction: {e}")
            print("Error: Please enter valid numbers.")
