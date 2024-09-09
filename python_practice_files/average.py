import statistics
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python average.py number1 number2 ...")
try:
    numbers = [int(arg) for arg in sys.argv[1:]]
    print(f"Mean is: {statistics.mean(numbers)}")
except ValueError:
    sys.exit("Error: All arguments must be numbers.")
