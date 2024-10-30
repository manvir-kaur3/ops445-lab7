#!/usr/bin/env python3
# Student ID: 115583221

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum_time = Time(0, 0, 0)
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second
    
    # Handle carry-over for seconds
    if sum_time.second >= 60:
        sum_time.minute += sum_time.second // 60
        sum_time.second %= 60

    # Handle carry-over for minutes
    if sum_time.minute >= 60:
        sum_time.hour += sum_time.minute // 60
        sum_time.minute %= 60

    return sum_time

def change_time(time, seconds):
    time.second += seconds

    # Handle seconds less than zero
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Handle carry-over for seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    # Handle minutes less than zero
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Handle carry-over for minutes
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def format_time(t):
    """Format time in HH:MM:SS."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

if __name__ == '__main__':
    # Example usage
    time1 = Time(9, 50, 0)
    seconds = 1800
    change_time(time1, seconds)
    print(format_time(time1))  # Should output '10:20:00'

    seconds = -1800
    change_time(time1, seconds)
    print(format_time(time1))  # Should output '09:50:00'
