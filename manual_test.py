#!/usr/bin/env python3
"""
Manual test script for Habit Tracker CLI Application
"""

import os
import sys
from habit_tracker import HabitTracker

def manual_test():
    """Manual test of the HabitTracker implementation."""
    # Use a test database
    test_db = "manual_test_habits.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("=== Habit Tracker Manual Test ===")
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Test adding habits
    print("\n1. Testing habit addition...")
    tracker.add_habits("Exercise, Drink Water, Read Books")
    
    # Test showing habits
    print("\n2. Testing habit display...")
    habits = tracker.get_habits()
    print("Current habits:")
    for habit_id, habit_name in habits:
        print(f"  {habit_id}: {habit_name}")
    
    # Test tracking habits
    print("\n3. Testing habit tracking...")
    tracker.track_habit(1, True)  # Mark first habit as done
    tracker.track_habit(2, False)  # Mark second habit as not done
    
    # Test showing calendar
    print("\n4. Testing calendar display...")
    tracker.show_calendar()
    
    # Test streak calculations
    print("\n5. Testing streak calculations...")
    current_streak_1 = tracker.calculate_current_streak(1)
    longest_streak_1 = tracker.calculate_longest_streak(1)
    print(f"Habit 1 - Current streak: {current_streak_1}, Longest streak: {longest_streak_1}")
    
    current_streak_2 = tracker.calculate_current_streak(2)
    longest_streak_2 = tracker.calculate_longest_streak(2)
    print(f"Habit 2 - Current streak: {current_streak_2}, Longest streak: {longest_streak_2}")
    
    # Test removing habits
    print("\n5. Testing habit removal...")
    tracker.remove_habits("1,2")  # Remove first two habits
    
    # Test showing habits again
    print("\n6. Testing habit display after removal...")
    habits = tracker.get_habits()
    print("Current habits:")
    for habit_id, habit_name in habits:
        print(f"  {habit_id}: {habit_name}")
    
    # Test showing calendar again
    print("\n7. Testing calendar display after removal...")
    tracker.show_calendar()
    
    # Clean up
    del tracker
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("\n=== Manual Test Completed Successfully ===")

if __name__ == "__main__":
    manual_test()