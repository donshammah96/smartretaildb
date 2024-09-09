def main():

    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

def convert(fraction):
    """
    Convert a fraction to a percentage.
    Args:
        fraction (str): A fraction in the form 'x/y'.
    Returns:
        int: The percentage representation of the fraction.
    Raises:
        ValueError: If values are not integers or x > y.
        ZeroDivisionError: If the denominator is zero.
    """
    try:
        x, y = map(int, fraction.split("/"))
        if y == 0:
            raise ZeroDivisionError("Division by 0 is not allowed")
        if x > y:
            raise ValueError("X cannot be greater than Y")
        return round((x / y) * 100)
    except ValueError:
        raise ValueError("Values should be integers and X should not be greater than Y")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by 0 is not allowed")

def gauge(percentage):
    """
    Determine the gauge reading based on the percentage.
    Args:
        percentage (int): The percentage value.
    Returns:
        str: The gauge reading ("E", "F", or percentage as a string).
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()