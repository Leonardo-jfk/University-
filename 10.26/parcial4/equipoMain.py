import equipoClass
import random
import os
import pickle

from parcial4.libroMain import add_in_orden
from parcial4.pantalonMain import cargar_archivo, mostrar_arreglo


def opcion():
    cadena = print("las opciones posibles: \n" + \
    " 1: Cargar un arreglo de objetos\n" + \
    " 2. Mostrar el contenido del arreglo\n" + \
    " 3. mostrar el monto total recaudado \n" + \
    " 4. genere un archivo binario\n" + \
    " 5. Mostrar el archivo generado\n" + \
    " Ingrese que le gusta: \n")
    return int(input(cadena))




def cargar_arreglo():
    vector = []
    n = int(input("cant de equipos: "))
    while n <= 0:
        print("atencion, debe ser positivo")
        n = int(input("cant de equipos: "))

    nombres = ["barcelona", "realMadrid", "atletico", "sevilla", "manchester", "liverpool", "bavaria"]

    for i in range(n):
        numero = random.randint(1,100)
        nombre = random.choice(nombres)
        edad = random.randint(12,17)
        nivel = random.randint(0,2)
        precio = random.randint(10,100)


        equipo = equipoClass.Equipo(numero, nombre, edad, nivel, precio)

        add_in_orden(vector, equipo)
    return vector

#  mantenga ordenado por nombre del equipo
def add_in_orden(vector, equipo):
    izq = 0
    der = len(vector)


    while izq < der:
        centro = (izq + der) // 2
        if vector[centro].nombre < equipo.nombre:
            izq = centro + 1
        else:
            der = centro

    vector[izq:izq] = [equipo]


def mostrar_arreglo(vector):
    cant = len(vector)
    for i in range(cant):
        print(vector[i])



# para cada edad y nivel de juego
def  crear_matriz(vector):
    cant = len(vector)
    edades = 6
    niveles = 3

    matriz = [[0] * niveles for i in range(edades)]

    for jugador in vector:
        edad = jugador.edad - 12
        nivel = jugador.nivel
        matriz[edad][nivel] += jugador.precio


    mostrar_arreglo(matriz)

def main():

    vector, matriz_montos = [], []
    vector_cargado = False
    response = -1

    print("velkommen!")
    while response != 0:
        response = opcion()
        if response == 1:
            vector = cargar_arreglo()
            vector_cargado = True

        if vector_cargado:
            if response == 2:
                mostrar_arreglo(vector)

            if response == 3:
                matriz_montos =  crear_matriz(vector)

            if matriz_montos:
                if response == 4:

                    mostrar_arreglo(vector)

                if response == 5:
                    mostrar_arreglo(vector)

            else:
                print("anda a crear la matriz, opcion 3")

        else:
            print("anda al 1er paso")


    print("ciao! ")


if __name__ == "__main__":
    main()