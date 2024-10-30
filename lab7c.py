class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(t):
    """Convert a Time object to seconds."""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert seconds to a Time object."""
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return Time(hour, minute, second)

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Change the time by a specified number of seconds."""
    time.second += seconds
    while time.second < 0 or time.minute < 0:  # Handle negative seconds and minutes
        if time.second < 0:
            time.second += 60
            time.minute -= 1
        if time.minute < 0:
            time.minute += 60
            time.hour -= 1
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# Additional helper function to validate time can be added here if necessary
# def valid_time(t):
#     return 0 <= t.hour and 0 <= t.minute < 60 and 0 <= t.second < 60

# Example usage (for testing, can be removed later):
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    print(format_time(t1))  # Should print '09:50:00'
    sec_t1 = time_to_sec(t1)
    print(sec_t1)  # Should print 35400
    t1_sec = sec_to_time(sec_t1)
    print(format_time(t1_sec))  # Should print '09:50:00'
