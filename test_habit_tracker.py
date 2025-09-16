#!/usr/bin/env python3
"""
Test script for Habit Tracker CLI
"""

import os
import sys
import subprocess
import tempfile
import shutil

def run_command(cmd):
    """Run a command and return the result."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def test_habit_tracker():
    """Test all functionality of the habit tracker."""
    print("Testing Habit Tracker CLI...")
    
    # Test help command
    print("1. Testing help command...")
    stdout, stderr, code = run_command("python habit_tracker.py help")
    if code != 0:
        print(f"FAIL: Help command failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Help command works")
    
    # Test add multiple habits
    print("2. Testing add multiple habits...")
    stdout, stderr, code = run_command("python habit_tracker.py add \"Test Habit 1,Test Habit 2,Test Habit 3\"")
    if code != 0:
        print(f"FAIL: Add multiple habits failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Add multiple habits works")
    
    # Test simplified track habit as done
    print("3. Testing simplified track habit as done...")
    stdout, stderr, code = run_command("python habit_tracker.py +1")
    if code != 0:
        print(f"FAIL: Simplified track habit as done failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Simplified track habit as done works")
    
    # Test simplified track habit as not done
    print("4. Testing simplified track habit as not done...")
    stdout, stderr, code = run_command("python habit_tracker.py -1")
    if code != 0:
        print(f"FAIL: Simplified track habit as not done failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Simplified track habit as not done works")
    
    # Test track habit as done with specific date
    print("5. Testing track habit as done with specific date...")
    stdout, stderr, code = run_command("python habit_tracker.py +1 on 15")
    if code != 0:
        print(f"FAIL: Track habit as done with specific date failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Track habit as done with specific date works")
    
    # Test track habit as not done with specific date
    print("6. Testing track habit as not done with specific date...")
    stdout, stderr, code = run_command("python habit_tracker.py -1 on 14")
    if code != 0:
        print(f"FAIL: Track habit as not done with specific date failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Track habit as not done with specific date works")
    
    # Test calendar view
    print("7. Testing calendar view...")
    stdout, stderr, code = run_command("python habit_tracker.py")
    if code != 0:
        print(f"FAIL: Calendar view failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Calendar view works")
    
    # Test remove multiple habits using rm alias
    print("8. Testing remove multiple habits with rm alias...")
    stdout, stderr, code = run_command("python habit_tracker.py rm 1,2,3")
    if code != 0:
        print(f"FAIL: Remove multiple habits failed with code {code}")
        print(f"stderr: {stderr}")
        return False
    print("PASS: Remove multiple habits works")
    
    print("All tests passed!")
    return True

if __name__ == "__main__":
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    original_dir = os.getcwd()
    os.chdir(script_dir)
    
    try:
        success = test_habit_tracker()
        if not success:
            sys.exit(1)
    finally:
        os.chdir(original_dir)