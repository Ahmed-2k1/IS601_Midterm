"""
history_manager.py

This module contains the HistoryManager class, which manages calculation history
by storing records in a CSV file. It provides functionalities to add, load, and clear
the history of calculations.

Classes:
    HistoryManager - A manager for handling calculation history.

Usage:
    from history_manager import HistoryManager
"""
import pandas as pd
import os

class HistoryManager:
    """
    A class to manage the history of calculations by storing them in a CSV file.

    Attributes:
        file_path (str): The path to the history CSV file.

    Methods:
        add_record(operation, num1, num2, result) - Adds a new record to the calculation history.
        load_history() - Loads the history of calculations from the CSV file.
        clear_history() - Clears all records from the calculation history.
    """

    def __init__(self, file_path='history.csv'):
        """
        Initializes the HistoryManager with a specified file path. If the file does not
        exist, it creates one with appropriate headers.

        Args:
            file_path (str): The path to the CSV file. Defaults to 'history.csv'.
        """
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.clear_history()  

    def add_record(self, operation, num1, num2, result):
        """
        Initializes the HistoryManager with a specified file path. If the file does not
        exist, it creates one with appropriate headers.

        Args:
            file_path (str): The path to the CSV file. Defaults to 'history.csv'.
        """
        df = self.load_history()
        new_record = pd.DataFrame([{
            'Operation': operation,
            'Num1': num1,
            'Num2': num2,
            'Result': result
        }])
        
        # Ensure non-empty DataFrames to prevent warnings in future Pandas versions
        if not df.empty:
            df = pd.concat([df, new_record], ignore_index=True).tail(5)
        else:
            df = new_record  # Initialize df if empty

        df.to_csv(self.file_path, index=False)

    def load_history(self):
        """
        Loads the calculation history from the CSV file.

        Returns:
            DataFrame: A pandas DataFrame containing the history of calculations.
        """
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        # Return an empty DataFrame with specified columns if file doesn't exist
        return pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result'])

    def show_history(self):
        """Display the history of calculations."""
        df = self.load_history()
        if df.empty:
            print("No history available.")
        else:
            print("Calculation History:\n", df)

    def clear_history(self):
        """
        Clears all records from the calculation history by creating an empty CSV file.
        """
        pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result']).to_csv(self.file_path, index=False)
        print("History cleared.")

    def delete_record(self, index):
        """Delete a specific record from the history by index."""
        df = self.load_history()
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(self.file_path, index=False)
            print(f"Record {index} deleted.")
        else:
            print("Invalid record index.")
