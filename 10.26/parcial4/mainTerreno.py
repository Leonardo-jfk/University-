import random
import os
import pickle
import claseTerreno

def cargar_arreglo():
    quantitat = int(input("wie viele lotes haben sie: "))
    namen = ["quentin", "nina", "martin", "simon", "hugo", "francois"]
    familien = ["miller", "nouer", "kross", "schwaiteiger", "schwarz"]
    orientaciones = ["Norte", "Sur", "Este", "Oeste"]
    vector = []

    for lote in range(quantitat):
        nombre = random.choice(namen) + random.choice(familien)
        numManzana = random.randint(1,35)
        numLote = random.randint(1,20)
        # orientacion = random.choice(orientaciones)
        orientacion = random.randint(1,4)
        superficie = random.randint(100,9999)
        monto = random.randint(100_000,999_999)

        vector.append(claseTerreno.Lote(nombre, numManzana, numLote, orientacion, superficie, monto))


    return vector




def mostrar_arreglo(vector):
    quantitat = len(vector)

    for lote in range(quantitat):
        print(vector[lote])




def crear_matriz(vector):
    orientaciones = 4
    manzanas = 35
    matriz = [[0] * orientaciones for i in range(manzanas)]
    quantitat = len(vector)
    cant_lote_m = 0

    m = int(input("superficie total vendida para una manzana m: "))
    if m in range(1, 36):



        for lote in vector:
            fila = lote.numManzana - 1
            columna = lote.orientacion - 1

            matriz[fila][columna] += lote.superficie
            if m == lote.numManzana:
                    cant_lote_m += lote.superficie


        print("superficie total vendida para una manzana m es!! : ", cant_lote_m)
        cant_lote_m = 0
        return matriz

    else:
        print("ich brauch deine kopf")
        return matriz




def mostrar_matriz(matrizConteo):
    filas = len(matrizConteo)
    columnas = len(matrizConteo[0])

    for i in range(filas):
        print(matrizConteo[i])


def crear_archivo(vector, nameOfFile):
    quantitat = len(vector)


    file = open(nameOfFile, "wb")
    # endOfFile = os.path.getsize(file)

    I1 = int(input("min num lote: "))
    I2 = int(input("max num lote: "))

    if 1 <= I1 < I2 <= 20 :
        for i in range(quantitat):
            if I1 < vector[i].numLote < I2:
                pickle.dump(vector[i], file)

    else:
        print("ich brauch deine kopf")

    file.close()


def mostrar_archivo(nameOfFile):

    if not os.path.exists(nameOfFile):
        print("die file ist nicht gemacht")
        return

    file = open(nameOfFile, "rb")
    endOfFile = os.path.getsize(nameOfFile)
    suma, cant = 0,0

    while file.tell() < endOfFile:
        loteX = pickle.load(file)
        print(loteX)
        suma += loteX.monto
        cant += 1

    if cant != 0:
        promedio = suma / cant
        print("promedio de venta: ", promedio)
    else:
        print("wo ist mein Geld ")

    file.close()


def main():


    print("velkommen!")

    antwort = -1
    vector_gemacht, archivoCreado = False, False
    vector, matrizConteo = [], []
    nameOfFile = "lotess.dat"

    while antwort != 0:
        print("Menu de opciones: ")
        print("  1: Cargar un arreglo de objetos ")
        print("  2: Mostrar el contenido del arreglo ")
        print("  3: acumular y mostrar la superficie total vendida ")
        print("  4: genere un archivo binario ")
        print("  5: Mostrar el archivo generado ")
        print()
        antwort = int(input("\t\tUnsere antwort, akcionnen: "))

        if antwort == 1:
            vector = cargar_arreglo()
            vector_gemacht = True

        if vector_gemacht:
            if antwort == 2:
                mostrar_arreglo(vector)

            if antwort == 3:
                matrizConteo = crear_matriz(vector)
                mostrar_matriz(matrizConteo)

            if antwort == 4:

                crear_archivo(vector, nameOfFile)
                archivoCreado = True
            if antwort == 5:
                if archivoCreado:
                    mostrar_archivo(nameOfFile)
                else:
                    print("macht die punkt 4! ")
        else:
            print("macht die vector, bitte")

    print("vielen dank fur die arbeit")


if __name__ == "__main__":
    main()