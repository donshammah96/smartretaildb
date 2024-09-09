import random

def get_valid_input(prompt):
    """
    Prompt the user for input and validate that it is a positive integer.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                continue
            else:
                return value
        except ValueError:
            continue

def main():
    # Prompt for the level
    n = get_valid_input("Level: ")

    # Generate a random number
    guess = random.randint(1, n)

    # Prompt for guesses until the correct number is guessed
    while True:
        x = get_valid_input("Guess: ")
        if x == guess:
            print("Just right!")
            break
        elif x < guess:
            print("Too small!")
        else:
            print("Too large!")

if __name__ == "__main__":
    main()