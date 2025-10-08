#!/usr/bin/env python3
"""
Extended test script for Habit Tracker streak functionality
"""

import sqlite3
import os
import gc
from datetime import datetime, timedelta
from habit_tracker import HabitTracker

def setup_test_data(tracker):
    """Set up test data with various streak patterns."""
    print("Setting up test data with various streak patterns...")
    
    # Add test habits
    tracker.add_habit("Habit with 3-day streak")
    tracker.add_habit("Habit with broken streak")
    tracker.add_habit("Habit with long streak")
    
    today = datetime.now().date()
    
    # For habit 1: Create a 3-day current streak (done today, yesterday, day before)
    for i in range(3):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        tracker.track_habit(1, True, date_str)
    
    # For habit 2: Create a broken streak (done 5 days ago to 3 days ago, then today)
    for i in range(3, 6):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        tracker.track_habit(2, True, date_str)
    # Also done today
    tracker.track_habit(2, True, today.strftime('%Y-%m-%d'))
    
    # For habit 3: Create a 7-day streak (done for the last 7 days)
    for i in range(7):
        date = today - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        tracker.track_habit(3, True, date_str)

def test_complex_streaks():
    """Test complex streak scenarios."""
    # Use a test database
    test_db = "test_complex_streaks.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Set up test data
    setup_test_data(tracker)
    
    # Show calendar view
    print("\nCalendar view with complex streaks:")
    tracker.show_calendar()
    
    # Test streak calculations
    print("\nTesting streak calculations for complex scenarios:")
    
    # Habit 1: Should have current streak of 3, longest streak of 3
    current_streak_1 = tracker.calculate_current_streak(1)
    longest_streak_1 = tracker.calculate_longest_streak(1)
    print(f"Habit 1 - Current streak: {current_streak_1}, Longest streak: {longest_streak_1}")
    assert current_streak_1 == 3
    assert longest_streak_1 == 3
    
    # Habit 2: Should have current streak of 1 (only today), longest streak of 3
    current_streak_2 = tracker.calculate_current_streak(2)
    longest_streak_2 = tracker.calculate_longest_streak(2)
    print(f"Habit 2 - Current streak: {current_streak_2}, Longest streak: {longest_streak_2}")
    assert current_streak_2 == 1
    assert longest_streak_2 == 3
    
    # Habit 3: Should have current streak of 7, longest streak of 7
    current_streak_3 = tracker.calculate_current_streak(3)
    longest_streak_3 = tracker.calculate_longest_streak(3)
    print(f"Habit 3 - Current streak: {current_streak_3}, Longest streak: {longest_streak_3}")
    assert current_streak_3 == 7
    assert longest_streak_3 == 7
    
    # Explicitly delete the tracker to ensure connection is closed
    del tracker
    gc.collect()  # Force garbage collection
    
    # Small delay to ensure connections are closed
    import time
    time.sleep(0.1)
    
    # Clean up
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("\nAll complex streak tests passed!")

if __name__ == "__main__":
    test_complex_streaks()