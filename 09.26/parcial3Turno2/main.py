import random
import classTicket


def crear_class(cant_de_tickets):

    vector = []
    for i in range(cant_de_tickets):

        codigo = str(random.randint(100, 1000))
        pasajero = random.randint(1000000, 9999999)
        paisDestino = random.randint(1,20)
        numeroAsiento = random.randint(1, 300)
        importe = random.randint(100, 10000)
        vector.append(classTicket.Ticket(codigo, pasajero, paisDestino, numeroAsiento, importe ))

    return vector


def mostrar_vector(vector):
    for item in range(len(vector)):
        print(vector[item])


def mostrar_mayor(vector):
    vectorMayors = list()
    num = int(input("Ingrese el num para comparar: "))
    for item in range(len(vector)):
        if vector[item].numeroAsiento > num:
            vectorMayors.append(vector[item])

    return vectorMayors


def ordenar(vector, checker):
    n = len(vector)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            # if vector[i].checker  > vector[j + 1].checker:
            if getattr(vector[j], checker) > getattr(vector[j + 1], checker):
                ordenado = False
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
        if ordenado:
            break


def vectorSuma(vector, checker):

    n = len(vector)
    t = int(input("numero de cantidad min del acumulador: "))
    vectorSuma = 20 * [0]
    vectorSumeMayors = list()


    for i in range(n):
        for j in range(20):
            if j == vector[i].paisDestino:
                vectorSuma[j] += 1

    for i in range(20):
        if vectorSuma[i] > t:
            print(f"Acumulator for pais destino: {i} is {vectorSuma[i]}")
    print(vectorSuma)


def findID(vector):

    id = int(input("Ingrese el ID del pasajero: "))
    for item in range(len(vector)):
        if vector[item].pasajero == id:
            print(f"número de asiento: {vector[item].numeroAsiento}")
            print(f"Pais destino: {vector[item].paisDestino}")
            break
        elif item == len(vector) - 1:
            print("there's no equial ID")





def main():

    responce, cant_de_tickets = -1, 0
    vector = None

    while responce != 0:
        print("1: cant de tickets")
        print("2: crear un arreglo")
        print("3: mostrar vector")
        print("4: mostrar tickets mayores de num")
        print("5: importe de cada pais")
        print("6: find an ID")
        print("0: salir")

        responce = int(input("Ingrese el numero: "))


        if responce == 1:

            cant_de_tickets = int(input("Ingrese la cantidad de tickets: "))

        if responce == 2:
            if cant_de_tickets != 0:
                vector = crear_class(cant_de_tickets)
            else:
                print("go to option 1")

        if responce == 3:
            if vector != None:
                print(mostrar_vector(vector))
            else:
                print("no creaste vector")


        ## b)
        #mostrar los datos de todos los tickets cuyo
        # número de asiento sea mayor a un valor num
        if responce == 4:
            if vector != None:
                vectorMayors = mostrar_mayor(vector)
                ordenar(vectorMayors, "codigo")
                mostrar_vector(vectorMayors)
            else:
                print("no creaste vector")


        # c)
        # importe acumulado que se cobró por cada posible país de destino
        #
        if responce == 5:
            if vector != None:
                vectorSumas = vectorSuma(vector, "paisDestino")
            else:
                print("no creaste vector")


        # d)
        # Determinar si existe un ticket cuyo número
        # de identificación del pasajero sea igual a id
        if responce == 6:
            if vector != None:
                findID(vector)
            else:
                print("no creaste vector")

if __name__ == "__main__":
    main()