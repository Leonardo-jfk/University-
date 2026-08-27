import random


def Cards():
    # Card(nom, coleur)

    class Card:
        def __init__(self, nombre, color):
            self.nombre = nombre
            self.color = color

        def __str__(self):
            return str(str(self.nombre) + " of " + self.color)


    coleur = random.choice(["Rouge", "or", "noir", "blanc"])
    nom = random.randint(1,13)
    return Card(nom, coleur)


def GiveCards(quantite):


    if quantite == 2:
        jouer1 = Cards()
        jouer2 = Cards()

    return jouer1, jouer2

def compareCard(card1, card2):

    puntos1, puntos2 = 0, 0
    cartaNombre1, cartaNombre2 = int(card1.nombre), int(card2.nombre)


    if cartaNombre1 == cartaNombre2:
        print("compare oro")

    elif cartaNombre1 < cartaNombre2:
        puntos2 += cartaNombre1 + cartaNombre2

    else:
        puntos1 += cartaNombre1 + cartaNombre2

    return puntos1, puntos2



# if __name__ == "__main__":
