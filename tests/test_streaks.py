#!/usr/bin/env python3
"""
Test script for Habit Tracker streak functionality
"""

import sqlite3
import os
import gc
from datetime import datetime, timedelta
from habit_tracker import HabitTracker

def test_streaks():
    """Test the streak functionality of the HabitTracker."""
    # Use a test database
    test_db = "test_streaks.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Test adding habits
    print("Testing habit addition...")
    assert tracker.add_habit("Exercise") == True
    assert tracker.add_habit("Meditation") == True
    
    # Test current streak when no data
    print("Testing current streak with no data...")
    current_streak = tracker.calculate_current_streak(1)
    assert current_streak == 0
    print(f"Current streak for habit 1: {current_streak}")
    
    # Test longest streak when no data
    print("Testing longest streak with no data...")
    longest_streak = tracker.calculate_longest_streak(1)
    assert longest_streak == 0
    print(f"Longest streak for habit 1: {longest_streak}")
    
    # Add some tracking data to create a streak
    print("Adding tracking data to create streaks...")
    
    # Mark habit 1 as done for today
    tracker.track_habit(1, True)  # Today
    
    # Test current streak (should be 1 for habit 1, 0 for habit 2)
    print("Testing current streak calculation...")
    current_streak_1 = tracker.calculate_current_streak(1)
    current_streak_2 = tracker.calculate_current_streak(2)
    print(f"Current streak for habit 1 (Exercise): {current_streak_1}")
    print(f"Current streak for habit 2 (Meditation): {current_streak_2}")
    
    # Current streak should be 1 for habit 1 and 0 for habit 2
    assert current_streak_1 == 1
    assert current_streak_2 == 0
    
    # Test longest streak (should be 1 for habit 1, 0 for habit 2)
    print("Testing longest streak calculation...")
    longest_streak_1 = tracker.calculate_longest_streak(1)
    longest_streak_2 = tracker.calculate_longest_streak(2)
    print(f"Longest streak for habit 1 (Exercise): {longest_streak_1}")
    print(f"Longest streak for habit 2 (Meditation): {longest_streak_2}")
    
    # Longest streak should be 1 for habit 1 and 0 for habit 2
    assert longest_streak_1 == 1
    assert longest_streak_2 == 0
    
    # Show calendar view
    print("\nCalendar view with streaks:")
    tracker.show_calendar()
    
    # Explicitly delete the tracker to ensure connection is closed
    del tracker
    gc.collect()  # Force garbage collection
    
    # Small delay to ensure connections are closed
    import time
    time.sleep(0.1)
    
    # Clean up
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("\nAll streak tests passed!")

if __name__ == "__main__":
    test_streaks()