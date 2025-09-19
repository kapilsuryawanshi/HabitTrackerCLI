#!/usr/bin/env python3
"""
Test script for Habit Tracker CLI Application
"""

import sqlite3
import os
import gc
from habit_tracker import HabitTracker

def test_habit_tracker():
    """Test the HabitTracker implementation."""
    # Use a test database
    test_db = "test_habits.db"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Test adding habits
    print("Testing habit addition...")
    assert tracker.add_habit("Test Habit 1") == True
    assert tracker.add_habit("Test Habit 2") == True
    assert tracker.add_habit("Test Habit 1") == False  # Should fail (duplicate)
    
    # Test getting habits
    print("Testing habit retrieval...")
    habits = tracker.get_habits()
    assert len(habits) == 2
    assert habits[0][1] == "Test Habit 1"
    assert habits[1][1] == "Test Habit 2"
    
    # Test tracking habits
    print("Testing habit tracking...")
    assert tracker.track_habit(1, True) == True
    assert tracker.track_habit(2, False) == True
    assert tracker.track_habit(99, True) == False  # Should fail (non-existent ID)
    
    # Test removing habits
    print("Testing habit removal...")
    assert tracker.remove_habit(1) == True
    assert tracker.remove_habit(99) == False  # Should fail (non-existent ID)
    
    # Verify habit was removed
    habits = tracker.get_habits()
    assert len(habits) == 1
    assert habits[0][1] == "Test Habit 2"
    
    # Explicitly delete the tracker to ensure connection is closed
    del tracker
    gc.collect()  # Force garbage collection
    
    # Small delay to ensure connections are closed
    import time
    time.sleep(0.1)
    
    # Clean up
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print("All tests passed!")

if __name__ == "__main__":
    test_habit_tracker()