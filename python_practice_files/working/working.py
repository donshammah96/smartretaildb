import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regular expression pattern to match the input format
    pattern = r'(\d{1,2}:\d{2}|\d{1,2}) (AM|PM) to (\d{1,2}:\d{2}|\d{1,2}) (AM|PM)'
    
    # Search for the pattern in the input string
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")
    
    # Extract the times and periods
    start_time, start_period, end_time, end_period = match.groups()
    
    # Convert the start time to 24-hour format
    start_24 = convert_to_24_hour(start_time, start_period)
    
    # Convert the end time to 24-hour format
    end_24 = convert_to_24_hour(end_time, end_period)
    
    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    # Split the time into hours and minutes
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours = int(time)
        minutes = 0
    
    # Validate the time
    if hours < 1 or hours > 12 or minutes < 0 or minutes >= 60:
        raise ValueError("Invalid time")
    
    # Convert to 24-hour format
    if period == "AM":
        if hours == 12:
            hours = 0
    else:  # PM
        if hours != 12:
            hours += 12
    
    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()