import os
import pickle
import random
import libroClase




def add_in_orden():
    #     se mantenga ordenado por ISBN.

    vector = []
    qualitat = int(input("wie viele Buche haben Sie? "))
    titulos = ["harry", "hobbit", "aleth", "torah", "talmud", "bereshit", "mishna"]
    autors = ["hashem", "moses", "david", "israel", "rabbi", "lubavich"]

    for libro in range(qualitat):


        ISBN = random.randint(1_000_000_000, 999_999_999_9)
        titulo = random.choice(titulos)
        autor = random.choice(autors)
        idioma = random.randint(1,5)
        precio = random.randint(10,100)


        izq, duplicate = 0, False
        der = len(vector)

        while izq < der:
            centro = (izq + der) // 2
            if vector[centro].ISBN < ISBN:
                izq = centro + 1

            elif vector[centro].ISBN > ISBN:
                der = centro

            else:
                duplicate = True
                break

        if not duplicate:
            vector[izq:izq] = [libroClase.Libro(ISBN, titulo, autor, idioma, precio)]

    return vector



def mostrar_arreglo(vector):
    qualitat = len(vector)

    for libro in range(qualitat):
        print(vector[libro])



def buscarYDescuento(vector):
    quantitat = len(vector)
    x = int(input("donne le code a trouver: "))
    cant_encontrados = 0

    for libro in range(quantitat):
        if vector[libro].ISBN == x:
            print("todos sus datos: ", vector[libro])
            print()
            cant_encontrados += 1
            #  el idioma del mismo es Francés,
            if vector[libro].idioma == 4:
                print("datos antes descuento: ", vector[libro])
                print()
                vector[libro].precio -= (vector[libro].precio / 100 )*22
                print("datos despues del descuento: ", vector[libro])



    if cant_encontrados == 0:
            print("No contamos con el libro <ISBN> pero no deje de visitar nuestra sección de ofertas!")







def crear_archivo(vector, nameOfFile):
    quantitat = len(vector)
    file = open(nameOfFile, "wb")

    a = input("donne nous autor que vous avez envie: ")
    p = int(input("donne nous le prix maximal: "))

    for libro in range(quantitat):
        if vector[libro].autor == a and vector[libro].precio <= p:
            pickle.dump(vector[libro], file)


    file.close()


def mostrar_archivo(nameOfFile):
    if not os.path.exists(nameOfFile):
        print("archivo no existe putain")
        print()
        return


    endOfFile = os.path.getsize(nameOfFile)

    if endOfFile == 0:
        print("le ficher est vide, fils de pute")
        print()
        return

    file = open(nameOfFile, "rb")
    cantLibros = 0

    while file.tell() < endOfFile:
        libro = pickle.load(file)
        print(libro)
        cantLibros += 1

    print()
    print("quantite de livres est: ", cantLibros)







    file.close()



def main():
    arregloCreado, archivo_creado = False, False

    response = -1
    vector = []
    print("Velkommen! ")
    while response != 0:
        print("menu de opciones: ")
        print("  1:  Cargar un arreglo de registros ")
        print("  2:  Mostrar todos los libros ")
        print("  3:  Buscar un vehículo por ISBN ")
        print("  4:  genere un archivo binario ")
        print("  5:  Mostrar el archivo generado ")
        print()
        response = int(input("\t\t votre response monsieur: "))


        if response == 1:
            vector = add_in_orden()
            arregloCreado = True

        if arregloCreado:
            if response == 2:
                mostrar_arreglo(vector)

            if response == 3:
                buscarYDescuento(vector)

            if response == 4:
                nameOfFile = "libroos.dat"
                crear_archivo(vector,nameOfFile)
                archivo_creado = True

            if response == 5:
                if archivo_creado:
                    mostrar_archivo(nameOfFile)
                else:
                    print("aller au 4eme")

        else:
            print("arrete petit, 1ere")

    print("Vielen dank! ")


if __name__ == "__main__":
    main()


