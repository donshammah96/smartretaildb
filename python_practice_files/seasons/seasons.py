from datetime import date, datetime
import inflect
import sys

def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    minutes = calculate_minutes(birth_date)
    print(f"{minutes_to_words(minutes)} minutes")

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60

def minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    words = words.replace(" and", "")
    words = words.capitalize()
    return words

if __name__ == "__main__":
    main()
