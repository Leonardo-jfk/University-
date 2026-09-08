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
    num = int(input("Ingrese el num para comparar: "))
    for item in range(len(vector)):
        if vector[item].numeroAsiento > num:
            print(vector[item])


def main():

    responce = -1

    while responce != 0:
        print("1: cant de tickets")
        print("2: crear un arreglo")
        print("3: mostrar vector")
        print("4: mostrar tickets mayores de num")
        print("0: salir")

        responce = int(input("Ingrese el numero: "))


        if responce == 1:
            cant_de_tickets = int(input("Ingrese la cantidad de tickets: "))

        if responce == 2:
            vector = crear_class(cant_de_tickets)

        if responce == 3:
            print(mostrar_vector(vector))


        ## b)
        if responce == 4:
            mostrar_mayor(vector)





if __name__ == "__main__":
    main()