import os
import pickle
import random
import pantalonClase




def cargar_arreglo():
    n = int(input("la quantite de produits: "))
    while n <= 0:
        print("allez autre fois espece de... ")
        n = int(input("la quantite de produits"))

    vector = []
    modelos = ["levis", "tony lama", "ariat", "harley", "dior", "ginavci"]
    duplicate = False


    for jean in range(n):
        codigo = random.randint(100,105)
        modelo = random.choice(modelos)
        largo = random.randint(30, 50)
        cintura = random.randint(30, 50)
        tela = random.randint(1, 3)
        stock = random.randint(30, 500)
        duplicate = False

        # izq, posicion = 0, 0
        # der = len(vector)
        # while izq < der:
        #
        #     centro = (izq + der) // 2
        #     if vector[centro].codigo < codigo:
        #         izq = centro + 1
        #     # elif vector[centro].codigo > codigo:
        #
        #         der = centro

        izq = 0
        der = len(vector)
        while izq < der:
            centro = (izq + der) // 2
            if vector[centro].codigo > codigo:
                der = centro
            else:  # plus petit OU égal : on cherche à droite
                izq = centro + 1
    # else:
            #     duplicate = True
            #     posicion = centro
            #     break

        # if not duplicate:
        # if izq > der:
        #     posicion = izq
        vector[izq:izq] = [pantalonClase.Pantalon(codigo, modelo, largo, cintura, tela, stock)]

    return vector


def mostrar_arreglo(vector):
    cant = len(vector)

    for jean in range(cant):
        print(vector[jean])




def disponibleMatriz(vector):
    cant = len(vector)
    cintura = 21
    largo = 21

    matriz = [[0] * largo for i in range(cintura)]
    u = int(input("stock superior a u unidades: "))
    for jean in vector:
            cintura = jean.cintura - 31
            largo = jean.largo - 31
            matriz[cintura][largo] += jean.stock



    for cintura in range(20):
        for largo in range(20):
            stockReal = matriz[cintura][largo]
            if stockReal > u:
                print(f"pantalon de talle:{cintura + 31 } y de largo:{largo + 31} dispone: {stockReal}")



    # mostrar_arreglo(matriz)
    return matriz


def cargar_archivo(vector, nameOfFile):
    cant = len(vector)

    file = open(nameOfFile, "wb")
    t = int(input("Le nom de tela que vouz cherchez: "))

    for jean in range(cant):
        if vector[jean].stock > 0 and vector[jean].tela == t:
            # pickle.dump(file, vector[jean])
            pickle.dump(vector[jean], file)


    file.close()

def mostrar_archivo(nameOfFile):

    if not os.path.exists(nameOfFile):
        print("fils de pute!")
        return
    endOfFile = os.path.getsize(nameOfFile)
    if endOfFile == 0:
        print("autre fils de pute!")
        return

    file = open(nameOfFile, "rb")
    promedio, sumaStock, cantStock = 0, 0, 0


    while file.tell() < endOfFile:
        pantalon = pickle.load(file)
        print(pantalon)
        sumaStock += pantalon.stock
        cantStock += 1

    if cantStock > 0:
        promedio = sumaStock / cantStock

    print("stock promedio: ", promedio)




    file.close()




def main():

    antworte = -1
    vector = []
    archivoHecho = False

    print("velkommen!")
    while antworte != 0:


        print("choisis une option sil vous plait")
        print("   1: Cargar un arreglo ")
        print("   2: Mostrar todos los elementos ")
        print("   3: stock disponible")
        print("   4: generar un archivo binario ")
        print("   5: Mostrar el archivo generado ")
        print("   0: adieu ")

        antworte = int(input("\t\tvotre choix: "))

        if antworte == 1:
            vector = cargar_arreglo()

        if vector:
            if antworte == 2:
                mostrar_arreglo(vector)

            if antworte == 3:
                disponibleMatriz(vector)

            if antworte == 4:
                nameOfFile = "pantoles.dat"
                cargar_archivo(vector, nameOfFile)
                archivoHecho = True

            if antworte == 5:
                if archivoHecho:
                    mostrar_archivo(nameOfFile)


        else:
            print("allez au 1ere! ")

if __name__ == "__main__":
    main()

