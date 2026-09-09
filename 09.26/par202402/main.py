import random
import classTubo


def crear_arreglo():

    n = int(input("give us the quantity of tubes: "))
    vector = list()

    for i in range(n):
        codigo = random.randint(100, 999)
        diameter = float(random.randint(1.00, 99.00))
        type = random.randint(1, 20)
        weight = random.randint(0.00 , 1000)
        ignifugo = random.choice(["si", "no"])


        vector.append(classTubo.Tubo(codigo, diameter, type, weight, ignifugo))
    print("the vector is created! ")
    print()

    return vector


def mostrar_arreglo(vector):
    n = len(vector)

    for i in range(n):
        print(vector[i])



def vector_ignifugos(vector):
    n = len(vector)
    vector_ignifugos = list()

    for i in range(n):
        if vector[i].ignifugo == "si":
            vector_ignifugos.append(vector[i])


    # mostrar_arreglo(vector_ignifugos)

    ordenar_arreglo(vector_ignifugos, "diameter" )


def ordenar_arreglo(vector, type):
    n = len(vector)
    total_weight = 0
    # vector_ignifugos = list()/

    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if getattr(vector[j], type) > getattr(vector[j + 1], type ):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

                ordenado = False

        if ordenado:
            break

    print(" ordinated by diameter: ")
    mostrar_arreglo(vector)
    for i in range(n):
        total_weight += vector[i].weight

    print("cantidad promedio: ", total_weight / n)



def arreglo_acumulacion(vector):
    n = len(vector)
    vector_acumulador = 20 * [0]

    a = int(input("give us the min num for accumulations: "))

    for i in range(20):
        for j in range(n):
            if vector[j - 1].type == i:
                vector_acumulador[i] += 1

    # mostrar_arreglo(vector_acumulador)

    for i in range(20):
        if vector_acumulador[i] > a:
            print(f"The type {i} has {vector_acumulador[i]} tubes ")

    return vector_acumulador



def check_value(vector):
    prod = int(input("give us a code to check: "))
    n = len(vector)

    for i in range(n):
        if vector[i].codigo == prod:
            print(f"The diameter is {vector[i].diameter} and the type is {vector[i].type}")
            print()
            return

    print("we couldn't find it")
    print()




def main():

    response = -1
    vector = None


    while response != 0:
        print("0: Salir")
        print("1: crear arreglo")
        print("2: mostrar arreglo")
        print("3: Mostrar los datos de todos los tubos ignífugos")
        print("4: Mostrar cuántos tubos se fabrican por cada tipo")
        print("5: Check if a number exists a code of product")

        response = int(input("give us a num to continue: "))

        if response == 1:
            vector = crear_arreglo()


        if response == 2:
            if vector:
                mostrar_arreglo(vector)
            else:
                print("go to the 1st step")


        # b)
        # Mostrar los datos de todos los tubos ignífugos
        if response == 3:
            if vector:
                vector_ignifugos(vector)
            else:
                print("go to the 1st step")

        # c)
        #Determine cuántos tubos se fabrican por cada tipo
        if response == 4:
            if vector:
                arreglo_acumulacion(vector)
            else:
                print("go to the 1st step")

        # d)
        # determinar si existe un tubo cuyo código de producto sea igual a prod
        if response == 5:
            if vector:
                check_value(vector)
            else:
                print("go to the 1st step")


if __name__ == "__main__":
    main()