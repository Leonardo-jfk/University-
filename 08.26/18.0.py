import random

def savePersonData(personData, quantity):
    personData = [0 for i in range(quantity)]
    personName = [0 for i in range(quantity)]
    personAge = [0 for i in range(quantity)]
    for person in range(quantity):
        personData[person] = int(input(f"Taille {person + 1}: "))
        personName[person] = input(f"Nom {person + 1}: ")
        personAge[person] = input(f"Age {person + 1}: ")

        # height = input(int(personData[person]))

    return personData, personName, personAge


def analysePersonData(personData):
    totalHeight, plusDeMoyeonne, moinDeMoyeonne = 0, 0, 0
    for person in range(len(personData)):
        totalHeight += personData[person]

    quantite = len(personData)
    moyeonne = totalHeight // quantite
    for person in range(quantite):
        if personData[person] > moyeonne:
            plusDeMoyeonne += 1
        else:
            moinDeMoyeonne += 1


    return moyeonne, plusDeMoyeonne, moinDeMoyeonne

def main():

    print("Voulez vous? ")
    if input("La reponse: y/n ") == "y":
    # if input("La reponse: y/n") in "yY":
        quantity = random.randint(2, 5)
        reponse = True
        personData, personName, personAge =  savePersonData(reponse, quantity)
        print(personData, personName, personAge)
    else:
        print("La reponse n'est pas voulez")


    if personData != None:
        # Dépaquetage direct des 3 valeurs dans 3 variables
        moyenne, au_dessus, en_dessous = analysePersonData(personData)

        # Vous pouvez ensuite les utiliser individuellement :
        print(f"Taille moyenne : {moyenne} cm")
        print(f"Nombre de personnes plus grandes : {au_dessus}")
        print(f"Nombre de personnes plus petites ou égales : {en_dessous}")
        # print( "ici", analysePersonData(personData))



if __name__ == "__main__":
    main()