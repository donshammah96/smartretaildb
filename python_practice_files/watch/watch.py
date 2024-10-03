import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python watch.py '<HTML>'")
    
    html = sys.argv[1]
    print(parse(html))

def parse(s):
    # Define a regular expression pattern to match the YouTube embed URL in the src attribute of an iframe
    pattern = r'<iframe[^>]+src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"'
    
    # Search for the pattern in the input string
    match = re.search(pattern, s)
    
    # If a match is found, convert the URL to the shorter youtu.be format
    if match:
        embed_url = match.group(1)
        video_id = embed_url.split('/')[-1]
        return f"https://youtu.be/{video_id}"
    
    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()