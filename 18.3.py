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

            medianoHelper1 = int(arregloTotal[(len(arregloTotal) - 1)// 2 ])
            medianoHelper2 = int(arregloTotal[(len(arregloTotal) + 1)// 2])
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
    secondListeModal = 0


    # for num1 in range(len(arregloTotal)):
    #     for num2 in range(len(arregloTotal) - 1):
    #         if arregloTotal[num1] == arregloTotal[num2 + 1]:
    #             counter1 += 1
    #
    #     if counter1 != 0:
    #             modelhelper.append(arregloTotal[num1])
    #             modelhelper.append(f"valeur:{counter1}")
    #     counter1 = 0\\\


    #
    # for num1 in range(len(arregloTotal) - 1):
    #     if arregloTotal[num1] == arregloTotal[num1 + 1]:
    #             counter1 += 1
    #     elif counter1 > counter2:
    #         counter2 = counter1
    #         modelhelper = arregloTotal[num1]
    #
    #         counter1 = 1
    #
    # if counter1 > counter2:
    #     modelhelper = arregloTotal[-1]
    #
    #
    #
    # print("reponse 3", modelhelper)
    #
    # if modelhelper == 1:
    #     return None
    #
    # return modelhelper
   #
   #  1.) Sea n la longitud del arreglo v.
   #  2.) Sea c otro vector de n componentes iniciado en cero.
   #  3.) Aplicar conteo de frecuencias de los valores de v, usando c como vector de conteo.
   #  4.) Sea idm (índice del posible valor modal) = 0.
   #  5.) Sea cfm (cantidad de veces que vimos la frecuencia máxima del posible valor modal) = 1
   #  6.) Para cada i en el rango de índices de c:
   #          6.1.) Si c[i] > c[idm]: (nueva frecuencia máxima encontrada).
   #                    6.1.1.) Sea idm = i (índice de la nueva posible moda).
   #                    6.1.2.) Sea cfm = 1 (conteo reseteado de la posible frecuencia máxima).
   #                sino:
   #                    6.1.3.) Si c[i] == c[idm]: (repetición de la posible frecuencia máxima...)
   #                                Sea cfm = cfm + 1 (contar esa repetición de la máxima...)
   #  7.) Si cfm == 1: (hay moda: la frecuencia máxima solo apareció una vez).
   #          7.1.) Sea moda = idm (el valor modal es el índice de c que contenía el mayor sin repetir).
   #      sino:
   #          7.2.) Sea moda = None (valor default para indicar que no hay moda).
   # 8.) Retornar moda.


  #
    print("autre", arregloRep)
    for num1 in range(n):
        for num2 in range(n):
            if arregloTotal[num1] == arregloTotal[num2 ]:
                arregloRep[num1] += 1


    for num2 in range(n):
        if arregloRep[num2] > arregloRep[num2 - 1]:
            modelMax = arregloRep[num2]

    modal = arregloTotal[modelMax]

    print("check: ", arregloRep)
    print("reponse 3l", modelMax)


    # for i in range(n):
    #     for j in range(n):
    #         if arregloRep[modelMax] != arregloTotal[modelMax]:
    #             print("trouve le meme")

    # faire 3eme liste, avec les valeurs qu'ils ont modelMax dans la 2eme liste
    for i in range(n):
        if arregloRep[i] == modelMax:
            arregloSameValue.append(arregloTotal[i])
            # secondListeModal = arregloTotal[i]
    print("reponse 4???", arregloSameValue)

    # comparer si les valeurs sont les memes par tous dans cette liste
    for num1 in range(1, len(arregloSameValue)):
        if arregloSameValue[num1] != arregloSameValue[num1 - 1]:
            return None


    if modelhelper == 1:
        return None

    return modelMax

def main():
    n = 3000
    medio, finalMedio, mediano, modal = 0, 0, 0, 0

    # arregloTotal = [ random.randint(1,100) for i in range(n) ]
    arregloTotal = [3, 3, 3, 6, 3, 3, 6, 7, 7, 7, 7, 7]

    finalMedio = (valorMedio(arregloTotal))
    print("reponse 1", finalMedio)


    mediano = (valorMediano(arregloTotal))
    print("reponse 2", mediano)

    modal = moda(arregloTotal)
    print("reponse 3", modal)


if __name__ == '__main__':
    main()