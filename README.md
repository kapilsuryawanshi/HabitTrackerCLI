# Habit Tracker CLI

A simple command-line habit tracking application written in Python. This application allows you to track your daily habits from the terminal with a minimal, efficient interface.

## Features

- **Add and remove multiple habits at once**: Add or remove multiple habits in a single command using comma-separated values
- **Flexible tracking**: Mark habits as done or not done for any date within the last 30 days using simple commands
- **Interactive check-in**: An interactive command to quickly update all habits for today in a guided process
- **Visual calendar view**: View a calendar-style visualization of your habit tracking history for the last 30 days
- **Streak tracking**: Track current and longest streaks for each habit with intuitive color coding
- **Data persistence**: All habit data stored in a SQLite database file (`habits.db`)
- **Minimal UX**: Simple interface with habit IDs for quick tracking
- **Color-coded feedback**: Visual indicators for tracking status and streak performance

## Installation

No installation required. The application only uses standard Python libraries and requires Python 3.x.

Simply run the script directly with Python:

```bash
python habit_tracker.py
```

## Usage

### Adding Habits

```bash
# Add new habits (comma-separated)
python habit_tracker.py add "Habit1,Habit2,Habit3"
```

### Removing Habits

```bash
# Remove habits by IDs (comma-separated)
python habit_tracker.py remove <id1,id2,id3>

# Or use the shorter alias
python habit_tracker.py rm <id1,id2,id3>
```

### Interactive Check-in

```bash
# Interactive check-in for all habits
python habit_tracker.py checkin

# Interactive check-in for a specific day (by day number)
python habit_tracker.py checkin on <day>
```

### Quick Tracking

```bash
# Mark a habit as done for today (by ID)
python habit_tracker.py +<habit_id>

# Mark a habit as done for a specific day (by ID)
python habit_tracker.py +<habit_id> on <day>

# Mark a habit as not done for today (by ID)
python habit_tracker.py -<habit_id>

# Mark a habit as not done for a specific day (by ID)
python habit_tracker.py -<habit_id> on <day>
```

### View Tracking

```bash
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

The habit tracker includes streak tracking features:

- **Current Streak**: Shows the number of consecutive days the habit has been completed up to today
- **Longest Streak**: Shows the longest consecutive streak of completions for the habit

### Color Coding for Streaks

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

The `checkin` command provides an interactive way to update all your habits for a specific day:

- Cycles through each habit one by one
- Shows the current status for the selected day (Done, Not done, or Not tracked yet)
- Prompts you to mark each habit as done (`y`), not done (`n`), or skip (`s`)
- Allows you to quit the check-in process at any time (`q`)

This is especially useful for daily routine tracking when you want to quickly update all your habits at once.

## Data Storage

Habit data is stored in a SQLite database file named `habits.db` in the same directory as the script. This database stores:
- Habit names and IDs
- Daily tracking records with dates and completion status
- No external dependencies required

## Commands Reference

| Command | Description |
|--------|-------------|
| `add <habit1,habit2,...>` | Add new habits (comma-separated) |
| `remove <id1,id2,...>` | Remove habits and their tracking history by IDs (comma-separated) |
| `rm <id1,id2,...>` | Alias for remove command |
| `checkin` | Cycle through all habits and track today's progress |
| `checkin on <day>` | Cycle through all habits and track for a specific day (by day number) |
| `+<id>` | Mark a habit as done for today (by ID) |
| `+<id> on <day>` | Mark a habit as done for a specific day (by ID) |
| `-<id>` | Mark a habit as not done for today (by ID) |
| `-<id> on <day>` | Mark a habit as not done for a specific day (by ID) |
| `help` | Show help message |
| `(no arguments)` | Display calendar view of habit tracking |

## Requirements

- Python 3.x
- Standard library modules (no external dependencies)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with Python and SQLite for efficient tracking and minimal dependencies.*