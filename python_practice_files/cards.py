import random

cards = ["jack", "queen", "king"]

def main():
    #sample with replacement
    print(random.choices(cards, k=2))



if __name__ == "__main__":
    main()