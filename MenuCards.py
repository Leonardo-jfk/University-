from funcCards import *

def main():

    print("Menu d'options: ")
    r =  int(input("choiez quoi faire? 1-jouer 2-commencer le jeu 3-fin du jeu 4-sortir ? "))

    if r == 1:

        c1 = Cards()
        print(c1)
    if r == 2:
        c2 = GiveCards(2)

        print(c2[0], c2[1])
        main()

    if r == 3:
        c2 = GiveCards(2)
        # c3 = compareCard(c2[0], c2[
        c3 = compareCard(c2[0], c2[1])

        print(c3)

    # elif r == 4:
    #     break
    #


if __name__ == "__main__":
    main()