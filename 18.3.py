import random

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

    print("avant", arregloTotal)
    for num1 in range(len(arregloTotal)):
        for num2 in range(len(arregloTotal)):
            if arregloTotal[num1] < arregloTotal[num2]:
                arregloTotal[num1], arregloTotal[num2] = arregloTotal[num2], arregloTotal[num1]

    print("apres", arregloTotal)

    if len(arregloTotal) != 0:
        if len(arregloTotal) % 2 == 0:

            medianoHelper1 = int(arregloTotal[(len(arregloTotal))// 2 ])
            medianoHelper2 = int(arregloTotal[(len(arregloTotal)// 2) + 1])
            mediano = (medianoHelper1 + medianoHelper2) / 2
            finalMediano = round(mediano, 2)
            return finalMediano

        else:
            finalMediano = arregloTotal[(len(arregloTotal))// 2 ]
            return finalMediano
    return arregloTotal

def moda(arregloTotal):
    modal, modelhelper, counter1, counter2 = 0, [], 0, 0


    for num1 in range(len(arregloTotal)):
        for num2 in range(len(arregloTotal) - 1):
            if arregloTotal[num1] == arregloTotal[num2 + 1]:
                counter1 += 1

        if counter1 != 0:
                modelhelper.append(arregloTotal[num1])
                modelhelper.append(f"valeur:{counter1}")
        counter1 = 0

    print("reponse 3", modelhelper)

    return modelhelper




def main():
    n = 31
    medio, finalMedio, mediano, modal = 0, 0, 0, 0

    arregloTotal = [ random.randint(1,100) for i in range(n) ]
    v = [3, 3, 3, 3, 6, 6, 7, 7]

    finalMedio = (valorMedio(arregloTotal))
    print("reponse 1", finalMedio)


    mediano = (valorMediano(arregloTotal))
    print("reponse 2", mediano)

    modal = moda(arregloTotal)
    print("reponse 3", modal)


if __name__ == '__main__':
    main()