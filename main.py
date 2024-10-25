"""
main.py

This module serves as the entry point for the application. It instantiates the App class
from the app module and starts the application when executed from the command line.

Usage:
    python main.py
"""

from app import App

if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App and start the application
    