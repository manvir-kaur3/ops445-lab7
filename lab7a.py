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

def format_time(t):
    """Format time in HH:MM:SS."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

if __name__ == '__main__':
    # Example usage
    t1 = Time(8, 0, 0)
    t2 = Time(0, 50, 0)
    t3 = Time(8, 55, 0)
    td = Time(0, 50, 0)

    tsum1 = sum_times(t1, td)
    tsum2 = sum_times(t3, td)
    tsum3 = sum_times(t2, td)

    ft = format_time
    print(ft(t1), '+', ft(td), '-->', ft(tsum1))
    print(ft(t3), '+', ft(td), '-->', ft(tsum2))
    print(ft(t2), '+', ft(td), '-->', ft(tsum3))
