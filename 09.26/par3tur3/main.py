
import random
import classServicio


## done with it in 1:50 hours

def cargar_arreglo():
    n = int(input("give us the number of servicios: "))
    vector = []
    names = ["alice", "margaux", "hugo", "simon", "dino", "martin", "michael"]


    for i in range(n):
        codeIdent = random.randint(100, 999)
        name = random.choice(names)
        typeOfServicio = random.randint(1, 10)
        importe =random.randint(100, 9999)

        vector.append(classServicio.Servicio(codeIdent, name, typeOfServicio, importe))

    return (vector)


def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])


def checkInRaneg(vector):
    i1 = int(input("give us the 1st number: "))
    i2 = int(input("give us the 2nd number: "))
    vectorRange = list()

    for i in range(len(vector)):
        if vector[i].importe in range(i1, i2):
            vectorRange.append(vector[i])

    return vectorRange


def ordenar(vector, tipo):
    n = len(vector)
    for i in range(n - 1):

        ordenado = True
        for j in range(n - i - 1):
            if getattr(vector[j], tipo) > getattr(vector[j + 1], tipo):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                ordenado = False

        if ordenado:
            break


def vectorCantServicio(vector):
    n = len(vector)
    vectorCantServicio = 10 * [0]
    vectorCantFinal = list()

    # for i in range(n):
    for j in range(10):
        for i in range(n):
            if vector[i].typeOfServicio - 1  == j:
                vectorCantServicio[j] += 1

    # print(vectorCantServicio)
    for i in range(len(vectorCantServicio)):
        print(vectorCantServicio[i])
        if vectorCantServicio[i] != 0:
            vectorCantFinal.append(vectorCantServicio[i])

    return vectorCantFinal



def findName(vector):
    n = len(vector)

    nom = input("give us the nom: ")
    found = False
    for i in range(n):
        if vector[i].name == nom:
            vector[i].importe += 2000
            client = i
            found = True
            return client
    if found == False:
        print("didn't find nom")


def mostrar_client(vector, client):
    n = len(vector)
    for i in range(n):
        if i == client:
            print(vector[i])

def main():

    responce = -1
    vector, vectorServicios = None, None

    while responce != 0:
        print("0: Salir")
        print("1: start, cargar arreglo")
        print("2: Check in range")
        print("3: Mostrar cant de cada servicio")
        print("4: Mostrar si existe client ")

        responce = int(input("give us the number: "))


        if responce == 1:
            vector = cargar_arreglo()
            mostrar_vector(vector)


        # b)
        #Mostrar los datos de todos los servicios
        # cuyo importe esté entre los valores i1 e i2 (ambos incluidos)
        if responce == 2:
            if vector != None:
                vectorRange = checkInRaneg(vector)
                mostrar_vector(vectorRange)
                ordenar(vectorRange, "codeIdent")

                print("Cantidad de Servicios: ", len(vectorRange))
                mostrar_vector(vectorRange)
            else:
                print("go to 1st and carge arreglo")


        # c)
        #Determinar cuántos servicios hay para uno de
        # los tipos posibles (10 contadores). Mostrar todos los conteos
        # que sean diferentes de cero.
        if responce == 3:
            if vector:
                vectorServicios = vectorCantServicio(vector)
                print("View the vector of servises: ")
                mostrar_vector(vectorServicios)


            else:
                print("go to 1st and carge arreglo")


        # d)
        # nombre de cliente sea igual a nom
        if responce == 4:
            if vector != None:
                client = findName(vector)
                print("The client is: ")
                mostrar_client(vector, client)

            else:
                print("go to 1st and carge arreglo")



if __name__ == "__main__":
    main()