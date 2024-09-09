import random

cards = ["jack", "queen", "king"]

def main():
    random.shuffle(cards)
    for  card in cards:
        print(card)



if __name__ == "__main__":
    main()