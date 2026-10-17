from tkinter.font import nametofont

from clase import *
import random
import pickle
import os.path


def add_in_order(e, v):
    der, izq, duplicado = len(v), 0, False

    while izq < der:
        centro = (izq + der) // 2
        if v[centro].nombre < e.nombre:
            izq = centro + 1
        elif v[centro].nombre > e.nombre:
            der = centro
        else:
            duplicado = True
            izq = centro
            break

    # if not duplicado:
    v[izq:izq] = [e]

def validar():
    n = int(input("un arreglo de objetos con los datos de n equipos: "))
    while n <= 0:
        print("error!")
        n = int(input("un arreglo de objetos con los datos de n equipos: "))

    return n

def cargar_vector(v):
#     ordenado por nombre del equipo
    n = validar()
    v.clear()
    nombres = ["real", "barcelona", "manchester", "bavaria", "PSG", "liverpool"]
    for i in range(n):
        num =  random.randint(100,999)
        nom = random.choice(nombres)
        edad = random.randint(12,17)
        niv = random.randint(0,2)
        monto = random.randint(10,100)

        equipo = Equipo(num, nom, edad, niv, monto)

        add_in_order(equipo, v)

    return v

def mostrar_vector(v):
    for equipo in v:
        print(equipo)


def validar_rango():
    pass


def acumular(v):
    # para cada edad y nivel de juego
    matriz = [ [0] * 3 for i in range(6)]
    e = int(input("ingrese la edad deseada: "))
    contador_de_e = 0

    for equipo in v:
        nivel = equipo.nivel
        edad = equipo.edad - 12

        matriz[edad][nivel] += equipo.monto

        if equipo.edad == e:
            contador_de_e += equipo.monto

    print("mostrar", contador_de_e)



def generar_archivo(v, i1, i2, nameOfFile):
    file = open(nameOfFile, "wb")

    for equipo in v:
        if i1 <= equipo.numero <= i2:
            pickle.dump(equipo, file)





    file.close()


def mostrar_archivo(nameOfFile):
    file = open(nameOfFile, "rb")

    contarEdad,contarCant  = 0, 0
    endOfFile = os.path.getsize(nameOfFile)
    while file.tell() < endOfFile:
        equipo = pickle.load(file)
        print(equipo)
        contarEdad += equipo.edad
        contarCant += 1

    if contarCant > 0:
        promedio = round(contarEdad / contarCant, 2)
        print("promedio es: ", promedio)



    file.close()

def principal():
    nameOfFile = "archivoLast.dat"
    op = 1
    v = []
    while op != 6:
        print("Menú de opciones")
        print("1-Cargar")
        print("2-Mostrar")
        print("3-Acumular")
        print("4-Generar archivo")
        print("5-Mostrar archivo")
        print("6-Salir")
        op = int(input("Ingrese su opción: "))
        if op == 1:
            v = cargar_vector(v)

        elif op == 6:
            print("Adiós!")

        elif len(v) == 0:
            print("Primero debe cargar el vector!")
        elif op == 2:
            mostrar_vector(v)
        elif op == 3:
            acumular(v)
        elif op == 4:

            i1 = int(input("Ingrese i1: "))
            i2 = int(input("Ingrese i2: "))
            while i1 >= i2:
                i1 = int(input("Ingrese i1 otra vez: "))
                i2 = int(input("Ingrese i2: "))
            generar_archivo(v, i1, i2, nameOfFile)
        elif op == 5:
            mostrar_archivo(nameOfFile)




if __name__ == "__main__":
    principal()