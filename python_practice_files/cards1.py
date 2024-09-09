import random

cards = ["jack", "queen", "king"]

def main():
    #sample without replacement
    print(random.sample(cards, k=2))



if __name__ == "__main__":
    main()