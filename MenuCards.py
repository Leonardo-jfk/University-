from funcCards import *
from rich import print, console
from rich.console import Console


# def gamer(name):

class GamerInfo:

            def __init__(self, name):
                self.name = name
                self.score = 0
                self.totalScore = 0
                self.totalGames = 0

            def __str__(self):
                return self.name


    # return GamerInfo




def main():
    menu = "MENU DU JEU"
    print(f"{menu:*^30}")


    # print("Menu d'options: ")
    r =  int(input("choiez quoi faire? 1-difener les joeurs 2-commencer le jeu 3-fin du jeu 4-sortir ? "))

    if r == 1:
        jouers = []
        for _ in range(2):
            # print("[bold yellow] === Donne deux prémons === [/bold yellow]")
            playerName = input(" === Donne deux prémons === ")
            player1 = GamerInfo(playerName)
            jouers.append(player1)
        # print(gamer())
        print(jouers[0], jouers[1])

    elif r == 2:
        c2 = GiveCards(2)

        print(c2[0], c2[1])
        main()

    elif r == 3:
        c2 = GiveCards(2)
        # c3 = compareCard(c2[0], c2[
        c3 = compareCardNum(c2[0], c2[1])

        print(c3)

    elif r == 4:
        print("vous avez sorti!")
        reponse = input("voulez vous continuer ?")
        if reponse == "y":
            main()

    # elif r == 4:
    #     break
    #


if __name__ == "__main__":
    main()