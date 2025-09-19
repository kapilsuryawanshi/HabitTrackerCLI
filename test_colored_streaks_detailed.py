#!/usr/bin/env python3
"""
Test script to demonstrate colored streaks with different values
"""

import os
import sys
from datetime import datetime, timedelta
from habit_tracker import HabitTracker

def test_colored_streaks_detailed():
    """Test the colored streak display with different streak values."""
    # Use a test database
    test_db = "colored_streaks_detailed_test.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("=== Testing Colored Streak Display ===")
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Test adding habits
    print("\n1. Adding test habits...")
    tracker.add_habits("Habit with equal streaks,Habit with broken streak")
    
    # Create a streak for habit 1: done for last 3 days
    today = datetime.now().date()
    for i in range(3):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        tracker.track_habit(1, True, date_str)
    
    # Create a broken streak for habit 2: done 5 days ago to 3 days ago, and today
    for i in range(3, 6):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        tracker.track_habit(2, True, date_str)
    # Also done today
    tracker.track_habit(2, True, today.strftime('%Y-%m-%d'))
    
    # Show calendar view
    print("\n2. Calendar view with colored streaks:")
    print("Legend:")
    print("  - Green numbers: Current streak equals longest streak")
    print("  - Red numbers: Current streak is less than longest streak")
    print("  - Yellow numbers: Longest streak")
    print()
    tracker.show_calendar()
    
    print("\nExpected results:")
    print("  - Habit 1: Current streak (3) = Longest streak (3) -> Green")
    print("  - Habit 2: Current streak (1) < Longest streak (3) -> Red")
    
    # Clean up
    del tracker
    if os.path.exists(test_db):
        try:
            os.remove(test_db)
        except:
            pass  # Ignore cleanup errors
    
    print("\n=== Test Completed ===")

if __name__ == "__main__":
    test_colored_streaks_detailed()