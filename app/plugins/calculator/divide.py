"""
divide.py

This module provides the Divide class to handle division operations in the calculator.
The result of the division is displayed and saved to the calculation history.

Classes:
    Divide - Executes division and stores the result in the history.

Usage:
    from divide import Divide
"""

import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Divide(Command):
    """
    A command to perform division between two numbers.

    Methods:
        execute() - Prompts for two numbers, divides them, displays the result, and stores it in history.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the division operation by taking user input for two numbers, calculating the quotient,
        and displaying and storing the result. Checks for division by zero.

        Raises:
            ValueError: If the input is not a valid number or division by zero is attempted.
        """

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
            logging.info(f"Dividing {num1} by {num2}: Result = {result}")
            print(f"The result of {num1} / {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Divide", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for division: {e}")
            print("Error:", e)
