"""
history_commands.py

This module provides classes to manage and display the calculation history in the calculator.
It includes commands to show, clear, and delete specific records in the history.

Classes:
    ShowHistory - Displays the calculation history.
    ClearHistory - Clears the entire calculation history.
    DeleteSpecificRecord - Deletes a specified record from the history.

Usage:
    from history_commands import ShowHistory, ClearHistory, DeleteSpecificRecord
"""

# history_commands.py (in calculator plugin)
from app.commands import Command
from app.history_manager import HistoryManager
import logging

class ShowHistory(Command):
    """
    A command to display the calculation history.

    Methods:
        execute() - Displays the current calculation history.
    """
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """Displays the calculation history by calling the history manager's show method."""
        print("\nCalculation History:")
        self.history_manager.show_history()

class ClearHistory(Command):
    """
    A command to clear the calculation history.

    Methods:
        execute() - Clears the entire history.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """Clears the calculation history by calling the history manager's clear method."""
        self.history_manager.clear_history()
        print("History has been cleared.")

class DeleteSpecificRecord(Command):
    """
    A command to delete a specific record from the calculation history.

    Methods:
        execute() - Deletes a specified record based on user input.
    """

    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Prompts the user for a record index to delete and removes the corresponding
        record from the calculation history.

        Raises:
            ValueError: If the input is not a valid number.
        """
        try:
            index = int(input("Enter the record index to delete: "))
            self.history_manager.delete_record(index)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
