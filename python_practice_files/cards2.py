import random

cards = ["jack", "queen", "king"]

def main():
    #sample with replacement and weights outcomes more in your favor
    print(random.choices(cards, weights=[75, 20, 5], k=1))



if __name__ == "__main__":
    main()