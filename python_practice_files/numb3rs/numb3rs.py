import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Split the IP address into parts
    parts = ip.split(".")
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a digit and within the range 0-255
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    
    return True

if __name__ == "__main__":
    main()