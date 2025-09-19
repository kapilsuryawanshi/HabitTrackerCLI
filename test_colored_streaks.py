#!/usr/bin/env python3
"""
Test script to demonstrate colored streaks
"""

import os
import sys
from habit_tracker import HabitTracker

def test_colored_streaks():
    """Test the colored streak display."""
    # Use a test database
    test_db = "colored_streaks_test.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("=== Testing Colored Streak Display ===")
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Test adding habits
    print("\n1. Adding test habits...")
    tracker.add_habits("Habit with equal streaks,Habit with broken streak")
    
    # Mark first habit as done for 3 consecutive days (current streak = longest streak = 3)
    print("\n2. Creating streaks...")
    tracker.track_habit(1, True)  # Today
    # Note: We can't easily simulate past dates without modifying more code
    
    # Show calendar view
    print("\n3. Calendar view with colored streaks:")
    tracker.show_calendar()
    
    # Clean up
    del tracker
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("\n=== Test Completed ===")

if __name__ == "__main__":
    test_colored_streaks()