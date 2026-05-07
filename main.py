"""
Main application entrypoint for Ouvidoria System.

This module initializes and runs the command-line menu interface.
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import the production menu
from menus.menuv2 import run_menu


def main():
    """Start the Ouvidoria application."""
    run_menu()


if __name__ == "__main__":
    main()