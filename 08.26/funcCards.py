import random


def Cards():
    # Card(nom, coleur)

    class Card:
        def __init__(self, nombre, color):
            self.nombre = nombre
            self.color = color

        def __str__(self):
            return str(str(self.nombre) + " of " + self.color)


    coleur = random.choice(["Rouge", "ORO", "noir", "blanc"])
    nom = random.randint(1,13)
    return Card(nom, coleur)


def GiveCards(quantite):


    if quantite == 2:
        jouer1 = Cards()
        jouer2 = Cards()

    return jouer1, jouer2

def compareCardNum(card1, card2):

    puntos1, puntos2 = 0, 0
    cartaNombre1, cartaNombre2 = int(card1.nombre), int(card2.nombre)



    if cartaNombre1 == cartaNombre2:
        print("compare oro")

    elif cartaNombre1 < cartaNombre2:
        puntos2 += cartaNombre1 + cartaNombre2

    else:
        puntos1 += cartaNombre1 + cartaNombre2

    return puntos1, puntos2

def compareCardColor(card1, card2):
    cardColor1, cardColor2 = card1.color, card2.color
    card1Won, Card2Won = False, False

    if cardColor1 == cardColor2:
        return print("empataron")
    elif cardColor1 == "ORO" and cardColor2 != "ORO":
        card1Won = True

        return card1Won

    elif cardColor2 == "ORO" and cardColor1 != "ORO":
        card2Won = True
        return card2Won

    else:
        card1Won, card2Won = False, False
        return print("empataron")


# if __name__ == "__main__":
