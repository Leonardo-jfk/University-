

import random
import classJuicio
#j'ai fait en 1 heure



def cargar_arreglo():
    n = int(input("Ingrese la cantidad de juicios: "))
    descripciones = ["muerto", "auto", "bici", "noche", "dia", "borracho"]
    nomberes = ["alice", "hugo", "margaux", "simon", "giulia"]
    vector = []

    for i in range(n):
        codeExp = random.randint(100,999)
        descripcion = random.choice(descripciones)
        type = random.randint(1,15)
        nomClient = random.choice(nomberes)
        monto = random.randint(1000,9999)

        vector.append(classJuicio.Juicio(codeExp, descripcion, type, nomClient, monto))


    return vector


def mostrar_mayor(vector):
    mon = int(input("Ingrese el numero de base: "))
    n = len(vector)
    vectorMayor = list()

    for i in range(n):
        if vector[i].monto > mon:
            vectorMayor.append(vector[i])

    n2 = len(vectorMayor)
    for i in range(n2 - 1):
        ordenado = True
        for j in range(n2 - i - 1):
            if vectorMayor[j].descripcion > vectorMayor[j + 1].descripcion:
                ordenado = False
                vectorMayor[j], vectorMayor[j + 1] = vectorMayor[j + 1], vectorMayor[j]

        if ordenado:
            break

    return vectorMayor



def mostrar_arreglo(vector):
    n = len(vector)

    for i in range(n):
        print(vector[i])


def crear_mayor(vector):
    n = len(vector)
    c = int(input("Ingrese el numero de base(mostrar mayores de): "))
    cantJuicios = 15 * [0]


    for i in range(n):
        for j in range(15):
            if vector[i].type - 1 == j:
                cantJuicios[j] += 1

    #mostrar_arreglo(cantJuicios)
    for i in range(15):
        if cantJuicios[i] > c:
            print(f"Contador para el type {i + 1} es {cantJuicios[i]}")


def find_juicio(vector):
    n = len(vector)
    cod = int(input("Ingrese el numero a encontrar: "))
    encontrado = False

    for i in range(n):
        if vector[i].codeExp == cod:
            nuevoMonto = int(input("Ingrese el numero de monto nuevo: "))
            vector[i].monto = nuevoMonto
            encontrado = True
            print(vector[i])
            return

    # if not encontrado:
    print("No se puede encontrar")

def main():


    response = -1
    while response != 0:
        print("0: Salir")
        print("1: Cargar el arreglo")
        print("2: Mostrar datos de todos los juicios")
        print("3: la cantidad de juicios que hay por cada tipo")
        print("4: si existe un juicio cuyo código de expediente sea igual a cod")
        print("5: Mostrar arreglo")

        response = int(input("Give us the number: "))


        if response == 1:
            vector = cargar_arreglo()
            if vector:
                print("Cargado correctamente")
                print()
            else:
                print("No se puede cargar")

        # b)
        if response == 2:
            if vector:
                vectorMayor = mostrar_mayor(vector)
                mostrar_arreglo(vectorMayor)
            else:
                print("carga el arreglo primero")

        # c)
        #Determinar y mostrar la cantidad de juicios que hay por cada posible tipo

        if response == 3:
            if vector:
                vectorCant = crear_mayor(vector)

            else:
                print("carga el arreglo primero")

        if response == 5:
            if vector:
                mostrar_arreglo(vector)
            else:
                print("carga el arreglo primero")


        # d)
        #si existe un juicio cuyo código de expediente sea igual a cod.
        if response == 4:
            find_juicio(vector)


if __name__ == "__main__":
    main()