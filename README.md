# Habit Tracker CLI

A simple command-line habit tracking application written in Python.

## Features

- Add and remove multiple habits at once
- Mark habits as done or not done for each day using simple commands
- Support for tracking habits on specific dates within the last 30 days
- View a calendar-style visualization of your habit tracking history
- Track current and longest streaks for each habit with color coding
- Interactive check-in command to quickly update all habits for today
- Data stored in a SQLite database
- Minimal UX with habit IDs for quick tracking

## Requirements

- Python 3.x

## Installation

No installation required. Just run the script directly with Python.

## Usage

```bash
# Add new habits (comma-separated)
python habit_tracker.py add "Habit1,Habit2,Habit3"

# Remove habits by IDs (comma-separated)
python habit_tracker.py remove <id1,id2,id3>
# or use the shorter alias
python habit_tracker.py rm <id1,id2,id3>

# Interactive check-in for all habits
python habit_tracker.py checkin

# Mark a habit as done for today (by ID)
python habit_tracker.py +<habit_id>

# Mark a habit as done for a specific day (by ID)
python habit_tracker.py +<habit_id> on <day>

# Mark a habit as not done for today (by ID)
python habit_tracker.py -<habit_id>

# Mark a habit as not done for a specific day (by ID)
python habit_tracker.py -<habit_id> on <day>

# View calendar of habit tracking (last 30 days)
python habit_tracker.py

# Show help
python habit_tracker.py help
```

## Calendar View

The calendar view shows the last 30 days of habit tracking:

- Habit IDs and names are listed in the first columns
- Following columns represent the last 30 days (day numbers only)
- Each cell shows the tracking status:
  - `D` (in green): Habit was done
  - `-`: Habit was not done or no data for that day
- The last two columns show the current streak and longest streak for each habit

## Streak Tracking

The habit tracker now includes streak tracking features:

- **Current Streak**: Shows the number of consecutive days the habit has been completed up to today
- **Longest Streak**: Shows the longest consecutive streak of completions for the habit

### Color Coding

The streak columns use color coding to provide visual feedback:

- **Green numbers**: Current streak equals longest streak (habit is maintaining its best performance)
- **Red numbers**: Current streak is less than longest streak (habit has a broken streak)
- **Yellow numbers**: Longest streak (always displayed in yellow for emphasis)

## Examples

```bash
# Add multiple habits
python habit_tracker.py add "Drink Water,Exercise,Reading"

# Remove multiple habits (using the IDs shown in the calendar view)
python habit_tracker.py remove 1,2,3
# or
python habit_tracker.py rm 1,2,3

# Interactive check-in for all habits
python habit_tracker.py checkin

# Track habits (using the IDs shown in the calendar view)
python habit_tracker.py +1         # Mark habit ID 1 as done for today
python habit_tracker.py +1 on 15   # Mark habit ID 1 as done for day 15
python habit_tracker.py -2         # Mark habit ID 2 as not done for today
python habit_tracker.py -2 on 15   # Mark habit ID 2 as not done for day 15

# View calendar with streak information
python habit_tracker.py
```

## Check-in Command

The `checkin` command provides an interactive way to update all your habits for today:

- Cycles through each habit one by one
- Shows the current status for today (Done, Not done, or Not tracked yet)
- Prompts you to mark each habit as done (y), not done (n), or skip (s)
- Allows you to quit the check-in process at any time (q)

This is especially useful for daily routine tracking when you want to quickly update all your habits at once.

## Data Storage

Habit data is stored in a SQLite database file named `habits.db` in the same directory as the script.

## Examples

```bash
# Add multiple habits
python habit_tracker.py add "Drink Water,Exercise,Reading"

# Remove multiple habits (using the IDs shown in the calendar view)
python habit_tracker.py remove 1,2,3
# or
python habit_tracker.py rm 1,2,3

# Track habits (using the IDs shown in the calendar view)
python habit_tracker.py +1         # Mark habit ID 1 as done for today
python habit_tracker.py +1 on 15   # Mark habit ID 1 as done for day 15
python habit_tracker.py -2         # Mark habit ID 2 as not done for today
python habit_tracker.py -2 on 15   # Mark habit ID 2 as not done for day 15

# View calendar
python habit_tracker.py
```