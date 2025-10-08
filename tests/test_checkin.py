#!/usr/bin/env python3
"""
Test script for the checkin command
"""

import os
import sys
from unittest.mock import patch
from io import StringIO
from habit_tracker import HabitTracker

def test_checkin():
    """Test the checkin functionality."""
    # Use a test database
    test_db = "checkin_test.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("=== Testing Checkin Command ===")
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Add some test habits
    print("\n1. Adding test habits...")
    tracker.add_habits("Exercise,Reading,Mediation")
    
    # Test the checkin method with mocked input
    print("\n2. Testing checkin with mocked responses...")
    
    # Mock the input responses for each habit
    with patch('builtins.input', side_effect=['y', 'n', 's']):
        result = tracker.checkin()
        print(f"Checkin result: {result}")
    
    # Show the calendar view to see the results
    print("\n3. Calendar view after checkin:")
    tracker.show_calendar()
    
    # Clean up
    del tracker
    if os.path.exists(test_db):
        try:
            os.remove(test_db)
        except:
            pass  # Ignore cleanup errors
    
    print("\n=== Test Completed ===")

if __name__ == "__main__":
    test_checkin()