#!/usr/bin/env python3
\"\"\"
Test script for checkin command with date functionality
\"\"\"\n
import os
import sqlite3
from habit_tracker import HabitTracker


def test_checkin_date_functionality():
    \"\"\"Test the checkin command with date functionality.\"\"\"
    # Use a test database
    test_db = \"test_checkin_date.db\"
    
    # Remove test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print(\"=== Testing checkin command with date functionality ===\")
    
    # Initialize the tracker
    tracker = HabitTracker(test_db)
    
    # Add a test habit
    print(\"\\n1. Adding a test habit...\")
    tracker.add_habit(\"Test Exercise\")
    
    # Manually track the habit for a few days to create some data
    print(\"\\n2. Tracking habit for a few days...\")
    from datetime import datetime, timedelta
    
    # Track for yesterday
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    tracker.track_habit(1, True, yesterday)
    
    # Track for today
    today = datetime.now().strftime('%Y-%m-%d')
    tracker.track_habit(1, True, today)
    
    print(f\"Tracked habit for {yesterday} and {today}\")
    
    # Test the _convert_day_to_date method to make sure it works
    print(\"\\n3. Testing _convert_day_to_date method...\")
    day_num = datetime.now().day
    result_date = tracker._convert_day_to_date(str(day_num))
    print(f\"Day {day_num} converted to: {result_date}\")
    
    # Test the _parse_date method
    print(\"\\n4. Testing _parse_date method...\")
    parsed_today = tracker._parse_date()
    print(f\"Parsed date with no input: {parsed_today}\")
    
    parsed_day = tracker._parse_date(str(day_num))
    print(f\"Parsed date with day {day_num}: {parsed_day}\")
    
    # Clean up
    if os.path.exists(test_db):
        os.remove(test_db)
    
    print(\"\\n=== Test completed successfully ===\")


if __name__ == \"__main__\":
    test_checkin_date_functionality()