import random
import classPublicacion





def cargar_arreglo():

    n = int(input("Give the number of publications: "))
    vector = n * [None]
    numbersCode = "qwertyuiopasdfghjklmnbvcxz"
    titulos = ["buch", "boker", "book", "libro", "livre"]

    for i in range(n):
        codigo = (random.choice(numbersCode) + str(random.randint(1,10)) + random.choice(numbersCode) + str(random.randint(1, 10)))
        titulo = random.choice(titulos)
        tipo = random.randint(1, 30)
        costo = random.randint(1000, 9999)

        vector[i] = classPublicacion.Publicacion(codigo, titulo, tipo, costo)

    print("vector is formed! ")
    print()
    return vector

def mostrar_arreglo(vector):
    num = len(vector)

    for i in range(num):
        print(vector[i])


def find_mayores(vector):
    n = len(vector)
    cos = int(input("give us the min cost: "))
    vectorMayors = list()

    for i in range(n):
        if vector[i].costo > cos:
            vectorMayors.append(vector[i])

    return vectorMayors

def ordenar_arreglo(vector, type):
    n = len(vector)

    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if getattr(vector[j], type) > getattr(vector[j + 1], type):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                ordenado = False

        if ordenado:
            break

    return vector




def crear_vector_cant(vector):
    n = len(vector)
    vector_cant = 30 * [0]

    x = int(input("give the min num for showing: "))

    for i in range(30):
        for j in range(n):
            if vector[j].tipo - 1 == i:
                vector_cant[i] += 1

    # mostrar_arreglo(vector_cant)

    for i in range(30):
        if vector_cant[i] > x:
            print(f"The type {i + 1} has {vector_cant[i]} publications ")

    # mostrar_arreglo(vector_cant)

    return vector_cant



def find_publicacion(vector):
    n = len(vector)
    nom = input("Give us the name of the publication to find: ")
    t = input("Give us the type of the publication to find: ")
    found = False

    for i in range(n):
        if str(vector[i].titulo) == nom and str(vector[i].tipo) == t:
            # found = True
            return print(vector[i])
    # if not found:
    print("Didn't find ")
    print()




def main():

    response = -1
    vector = None

    while response != 0:
        print("1: Cargar el arreglo")
        print("2: Mostrar arreglo")
        print("3: Mostrar los datos de publicaciones costo sea mayor")
        print("4: cantidad de publicaciones por tipo")
        print("5: Buscar una publicacion cuyo título coincida con nom ")
        print("0: Salir")
        response = int(input("give the numero que quiere: "))

        if response == 1:
            vector = cargar_arreglo()

        if response == 2:
            if vector:
                mostrar_arreglo(vector)
            else:
                print("go to the 1st step")

        # b)
        if response == 3:
            if vector:
                vectorMayors = find_mayores(vector)
                vectorMayorsFinal = ordenar_arreglo(vectorMayors, "codigo")

                mostrar_arreglo(vectorMayorsFinal)


            else:
                print("go to the 1st step")

        # c)
        #Determine la cantidad de publicaciones que hay por cada tipo
        if response == 4:
            if vector:
                vector_cant = crear_vector_cant(vector)
            else:
                print("go to the 1st step")


        #Buscar una publicacion cuyo título coincida con nom
        if response == 5:
            if vector:
                find_publicacion(vector)

            else:
                print("go to the 1st step")


if __name__ == "__main__":
    main()

