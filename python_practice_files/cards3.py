import random

cards = ["jack", "queen", "king", "ace"]


def main():
    # guarantee certain outcomes when you want to debugg your program using a seed(pseudo random number generator)
    random.seed(3)
    print(random.choices(cards, k=2))


if __name__ == "__main__":
    main()
