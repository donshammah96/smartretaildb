def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6) or not s[:2].isalpha() or not s.isalnum():
        return False
    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            has_number = True
            if char == '0' and i == len(s) - len(s.lstrip('0')):
                return False
        elif has_number:
            return False
    return True

if __name__ == "__main__":
    main()