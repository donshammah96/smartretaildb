import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python um.py '<text>'")
    
    text = sys.argv[1]
    print(count(text))

def count(s):
    # Define a regular expression pattern to match the word "um" case-insensitively
    pattern = r'\bum\b'
    
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, s, re.IGNORECASE)
    
    # Return the number of matches
    return len(matches)

if __name__ == "__main__":
    main()