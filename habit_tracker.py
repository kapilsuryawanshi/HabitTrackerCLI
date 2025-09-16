#!/usr/bin/env python3
"""
Habit Tracker CLI Application
Track your daily habits from the command line
"""

import argparse
import sqlite3
import sys
import os
from datetime import datetime, timedelta
from typing import List, Tuple

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RESET = '\033[0m'


class HabitTracker:
    def __init__(self, db_path: str = "habits.db"):
        """Initialize the HabitTracker with a database connection."""
        self.db_path = db_path
        self.init_db()

    def _get_db_connection(self):
        """Create and return a database connection with a context manager."""
        return sqlite3.connect(self.db_path)
        
    def init_db(self):
        """Initialize the database with required tables."""
        try:
            with self._get_db_connection() as conn:
                # Create habits table
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS habits (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL
                    )
                ''')
                
                # Create tracking table
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS tracking (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        habit_id INTEGER,
                        date TEXT NOT NULL,
                        done BOOLEAN NOT NULL,
                        FOREIGN KEY (habit_id) REFERENCES habits (id),
                        UNIQUE(habit_id, date)
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise

    def add_habits(self, names: str) -> bool:
        """Add new habits to track from a comma-separated string."""
        # Split the names by comma and strip whitespace
        habit_names = [name.strip() for name in names.split(',')]
        
        success_count = 0
        for name in habit_names:
            if self.add_habit(name):
                success_count += 1
                
        total_count = len(habit_names)
        if success_count == total_count:
            print(f"All {total_count} habits added successfully!")
            return True
        else:
            print(f"Added {success_count} out of {total_count} habits.")
            return False

    def add_habit(self, name: str) -> bool:
        """Add a new habit to track."""
        try:
            with self._get_db_connection() as conn:
                conn.execute('INSERT INTO habits (name) VALUES (?)', (name,))
                print(f"Habit '{name}' added successfully!")
                return True
        except sqlite3.IntegrityError:
            print(f"Error: Habit '{name}' already exists!")
            return False
        except Exception as e:
            print(f"Error adding habit: {e}")
            return False

    def remove_habits(self, ids_str: str) -> bool:
        """Remove habits and their tracking history by comma-separated IDs."""
        # Split the IDs by comma and convert to integers
        try:
            habit_ids = [int(id_str.strip()) for id_str in ids_str.split(',')]
        except ValueError:
            print("Error: Invalid habit ID format. Please provide comma-separated numbers.")
            return False
        
        success_count = 0
        for habit_id in habit_ids:
            if self.remove_habit(habit_id):
                success_count += 1
                
        total_count = len(habit_ids)
        if success_count == total_count:
            print(f"All {total_count} habits removed successfully!")
            return True
        else:
            print(f"Removed {success_count} out of {total_count} habits.")
            return False

    def remove_habit(self, habit_id: int) -> bool:
        """Remove a habit and its tracking history by ID."""
        try:
            with self._get_db_connection() as conn:
                # First get the habit name
                result = conn.execute('SELECT name FROM habits WHERE id = ?', (habit_id,)).fetchone()
                
                if not result:
                    print(f"Error: Habit with ID {habit_id} not found!")
                    return False
                    
                habit_name = result[0]
                
                # Delete tracking records
                conn.execute('DELETE FROM tracking WHERE habit_id = ?', (habit_id,))
                
                # Delete the habit
                conn.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
                
                print(f"Habit '{habit_name}' (ID: {habit_id}) and its tracking history removed successfully!")
                return True
        except Exception as e:
            print(f"Error removing habit: {e}")
            return False

    def track_habit(self, habit_id: int, done: bool, date_str: str = None) -> bool:
        """Track a habit as done or not done for a specific date by ID."""
        try:
            with self._get_db_connection() as conn:
                # Get habit name
                result = conn.execute('SELECT name FROM habits WHERE id = ?', (habit_id,)).fetchone()
                
                if not result:
                    print(f"Error: Habit with ID {habit_id} not found!")
                    return False
                    
                habit_name = result[0]
                
                # Determine the date to use
                if date_str:
                    # Validate and convert the date
                    target_date = self._convert_day_to_date(date_str)
                    if not target_date:
                        return False
                else:
                    # Use today's date
                    target_date = datetime.now().strftime('%Y-%m-%d')
                
                # Insert or update tracking record
                conn.execute('''
                    INSERT OR REPLACE INTO tracking (habit_id, date, done)
                    VALUES (?, ?, ?)
                ''', (habit_id, target_date, done))
                
                status = "done" if done else "not done"
                date_display = datetime.strptime(target_date, '%Y-%m-%d').strftime('%Y-%m-%d')
                print(f"Habit '{habit_name}' (ID: {habit_id}) tracked as {status} for {date_display}!")
                return True
        except Exception as e:
            print(f"Error tracking habit: {e}")
            return False

    def _convert_day_to_date(self, day_str: str) -> str:
        """Convert a day number (within last 30 days) to a full date string."""
        try:
            day = int(day_str)
        except ValueError:
            print(f"Error: Invalid day '{day_str}'. Please provide a number.")
            return None
            
        # Generate the last 30 days
        dates = []
        date_objects = []
        for i in range(29, -1, -1):  # From 29 days ago to today
            date_obj = datetime.now() - timedelta(days=i)
            dates.append(date_obj.strftime('%Y-%m-%d'))
            date_objects.append(date_obj)
            
        # Find the date that matches the day number
        for date_obj, date_str in zip(date_objects, dates):
            if date_obj.day == day:
                return date_str
                
        print(f"Error: Day {day} is not within the last 30 days.")
        return None

    def get_habits(self) -> List[Tuple[int, str]]:
        """Get all habits."""
        try:
            with self._get_db_connection() as conn:
                return conn.execute('SELECT id, name FROM habits ORDER BY id').fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving habits: {e}")
            return []

    def get_tracking_data(self, habit_id: int, dates: List[str]) -> dict:
        """Get tracking data for a habit for specific dates."""
        try:
            with self._get_db_connection() as conn:
                # Create placeholders for the dates
                placeholders = ','.join('?' * len(dates))
                query = f'''
                    SELECT date, done FROM tracking 
                    WHERE habit_id = ? AND date IN ({placeholders})
                '''
                
                results = conn.execute(query, [habit_id] + dates).fetchall()
                
                # Convert to dictionary for easy lookup
                return {date: done for date, done in results}
        except sqlite3.Error as e:
            print(f"Error retrieving tracking data: {e}")
            return {}

    def show_calendar(self):
        """Display a calendar view of habit tracking for the last 30 days."""
        habits = self.get_habits()
        
        if not habits:
            print("No habits found. Add some habits to start tracking!")
            return
        
        # Generate last 30 days
        dates = []
        for i in range(29, -1, -1):  # From 29 days ago to today
            date = datetime.now() - timedelta(days=i)
            dates.append(date.strftime('%Y-%m-%d'))
        
        # Get date headers (just the day numbers)
        date_headers = [datetime.strptime(date, '%Y-%m-%d').strftime('%d') for date in dates]
        
        # Print header
        print(f"{'ID':<3} {'Habit':<16} " + " ".join(f"{day:>2}" for day in date_headers))
        print("-" * (20 + 30 * 3))
        
        # Print each habit's tracking data
        for habit_id, habit_name in habits:
            tracking_data = self.get_tracking_data(habit_id, dates)
            
            # Build row data
            row = f"{habit_id:<3} {habit_name:<16} "
            for date in dates:
                if date in tracking_data:
                    if tracking_data[date]:  # Done
                        row += f" {Colors.GREEN}D{Colors.RESET} "
                    else:  # Not done (show as -)
                        row += " - "
                else:  # No data
                    row += " - "
            
            print(row)

    def show_help(self):
        """Display detailed help information."""
        help_text = """
Habit Tracker CLI - Detailed Help

Commands:
  add <habit1,habit2,...>  Add new habits (comma-separated)
  remove <id1,id2,...>     Remove habits and their tracking history by IDs (comma-separated)
  rm <id1,id2,...>         Alias for remove command
  +<id>                    Mark a habit as done for today (by ID)
  +<id> on <day>           Mark a habit as done for a specific day (by ID)
  -<id>                    Mark a habit as not done for today (by ID)
  -<id> on <day>           Mark a habit as not done for a specific day (by ID)
  help                     Show this help message
  (no arguments)           Display calendar view of habit tracking

Calendar View:
  - Habit IDs and names are listed in the first columns
  - Following columns represent the last 30 days
  - Each cell shows the tracking status:
    D  Green D: Habit was done
    -  Dash: Habit was not done or no data for that day

Examples:
  python habit_tracker.py add "Drink Water,Exercise,Reading"
  python habit_tracker.py remove 1,2,3
  python habit_tracker.py rm 1,2,3
  python habit_tracker.py +1
  python habit_tracker.py +1 on 15
  python habit_tracker.py -1
  python habit_tracker.py -1 on 15
  python habit_tracker.py
        """
        print(help_text)

    def parse_short_command(self, command_args: List[str]) -> bool:
        """Parse and execute short commands like +1 or -1 with optional date."""
        if not command_args:
            return False
            
        command_str = command_args[0]
        
        # Parse date parameter if provided
        date_str = None
        if len(command_args) > 1:
            if len(command_args) >= 3 and command_args[1].lower() == 'on':
                date_str = command_args[2]
            else:
                print("Invalid command format. Use +<id> [on <date>] or -<id> [on <date>]")
                return False
        
        if command_str.startswith('+'):
            try:
                habit_id = int(command_str[1:])
                return self.track_habit(habit_id, True, date_str)
            except ValueError:
                print("Invalid habit ID. Use a number after +")
                return False
        elif command_str.startswith('-'):
            try:
                habit_id = int(command_str[1:])
                return self.track_habit(habit_id, False, date_str)
            except ValueError:
                print("Invalid habit ID. Use a number after -")
                return False
        else:
            print("Invalid command format. Use +<id> or -<id>")
            return False


def main():
    # Check if it's a short command like +1 or -1
    if len(sys.argv) >= 2 and sys.argv[1].startswith(('+', '-')):
        tracker = HabitTracker()
        tracker.parse_short_command(sys.argv[1:])
        return
    
    parser = argparse.ArgumentParser(
        description="Habit Tracker CLI - Track your daily habits",
        prog="habit_tracker.py",
        add_help=False  # We'll handle help ourselves
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add new habits (comma-separated)')
    add_parser.add_argument('habits', help='Names of habits to add (comma-separated)')
    
    # Remove command
    remove_parser = subparsers.add_parser('remove', aliases=['rm'], help='Remove habits by IDs (comma-separated)')
    remove_parser.add_argument('habit_ids', help='IDs of habits to remove (comma-separated)')
    
    # Help command
    subparsers.add_parser('help', help='Show this help message')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize habit tracker
    tracker = HabitTracker()
    
    # Handle commands
    if args.command == 'add':
        tracker.add_habits(args.habits)
    elif args.command in ['remove', 'rm']:
        tracker.remove_habits(args.habit_ids)
    elif args.command == 'help':
        tracker.show_help()
    elif args.command is None:
        # No command provided, show calendar view
        tracker.show_calendar()
    else:
        # Invalid command
        parser.print_help()


if __name__ == "__main__":
    main()