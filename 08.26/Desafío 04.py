import soporte

def valorMedio(arregloTotal):
    finalPromedio = 0

    sumaTotal, promedio = 0, 0
    for num in range(len(arregloTotal)):
        sumaTotal += arregloTotal[num]

    promedio = sumaTotal / len(arregloTotal)
    finalMedio = round(promedio, 2)
    return finalMedio


def valorMediano(arregloTotal):
    finalMediano, mediano, medianoHelper1, medianoHelper2 = 0, 0, 0, 0

    # print("avant", arregloTotal)
    for num1 in range(len(arregloTotal)):
        for num2 in range(len(arregloTotal)):
            if arregloTotal[num1] < arregloTotal[num2]:
                arregloTotal[num1], arregloTotal[num2] = arregloTotal[num2], arregloTotal[num1]

    # print("apres", arregloTotal)

    if len(arregloTotal) != 0:
        if len(arregloTotal) % 2 == 0:

            medianoHelper1 = arregloTotal[(len(arregloTotal) - 1)// 2]
            medianoHelper2 = arregloTotal[(len(arregloTotal) + 1)// 2]
            mediano = (medianoHelper1 + medianoHelper2) / 2

            finalMediano = round(mediano, 2)
            return finalMediano

        else:
            finalMediano = arregloTotal[(len(arregloTotal))// 2 ]
            return finalMediano
    return arregloTotal

def moda(arregloTotal):
    modal, modelhelper, counter1, counter2, modelMax, arregloRepHelper = 0, 0, 1, 1, 0, 0
    arregloRep = len(arregloTotal) * [0]
    n = len(arregloTotal)
    arregloSameValue = []
    modalReal = 0

    # print("autre", arregloRep)
    for num1 in range(n):
        for num2 in range(n):
            if arregloTotal[num1] == arregloTotal[num2 ]:
                arregloRep[num1] += 1


    for num2 in range(n):
        if arregloRep[num2] > arregloRep[num2 - 1]:
        # if arregloRep[num2] > modelMax:
            modelMax = arregloRep[num2]
            modalReal = arregloTotal[num2]

    # modal = arregloTotal[modelMax]

    # print("check: ", arregloRep)
    # print("reponse 3l", modalReal)

    # faire 3eme liste, avec les valeurs qu'ils ont modelMax dans la 2eme liste
    for i in range(n):
        if arregloRep[i] == modelMax:
            arregloSameValue.append(arregloTotal[i])
            # secondListeModal = arregloTotal[i]
    # print("reponse 4???", arregloSameValue)

    # comparer si les valeurs sont les memes par tous dans cette liste
    for num1 in range(1, len(arregloSameValue)):
        if arregloSameValue[num1] != arregloSameValue[num1 - 1]:
            return None

    #
    # if modelhelper == 1:
    #     return None

    return modalReal

def main():
    n = 3000
    medio, finalMedio, mediano, modal = 0, 0, 0, 0
    # arregloTotal = [3, 3, 3, 3, 6, 6, 7, 7, 67,7 ]
    # arregloTotal =   [3, 3, 3, 3, 6, 6, 7, 7]
    arregloTotal = soporte.vector_known_range(3000)
    # arregloTotal = [1, 3, 3, 8, 3, 3, 6, 6, 7, 7, 6, 7, 9]

    finalMedio = (valorMedio(arregloTotal))
    print("Reponse 1: ", finalMedio)

    mediano = (valorMediano(arregloTotal))
    print("Reponse 2: ", mediano)

    modal = moda(arregloTotal)
    print("Reponse 3: ", modal)


if __name__ == '__main__':
    main()