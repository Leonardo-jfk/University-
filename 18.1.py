import random

def avoirFiches():
    listeFiches1 = [random.randint(1, 15) for i in range(5)]
    listeFiches2 = [random.randint(1, 15) for i in range(5)]
    listeFiches3 = []

    for num in range(len(listeFiches1)):
        for num2 in range(len(listeFiches2)):
            if listeFiches1[num] == listeFiches2[num2]:
                listeFiches3.append(listeFiches1[num])

    return listeFiches3


def main():
    reponse = input("Voulez vous ?")
    if reponse == "y":
        reponse = True
        ficherFait = avoirFiches()

    else:
        reponse = False

    print(ficherFait)
if __name__ == "__main__":
    main()