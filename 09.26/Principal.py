#import Modulo_Alumno
from Modulo_Alumno import *

def cargar_vector(cant):
    vec = []
    for i in range(cant):
        leg = int(input("Ingrese un legajo: "))
        nom = input("Ingrese un nombre: ")
        pro = float(input("Ingrese un promedio: "))
        #aux = Modulo_Alumno.Alumno(leg, nom, pro)
        aux = Alumno(leg, nom, pro)
        vec.append(aux)
    return vec

def mostrar_vector(vec):
    for i in range(len(vec)):
        print(vec[i])

def mostrar_vector_may8(vec):
    for i in range(len(vec)):
        if vec[i].promedio > 8:
            print(vec[i])

def ordenar_vector(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].legajo > v[j].legajo:
                v[i], v[j] = v[j], v[i]

def contar_notas(vec):
    cont_notas = 10 * [0]
    for i in range(len(vec)):
        sub = int(vec[i].promedio - 1)
        cont_notas[sub] += 1
    return cont_notas

def programa():
    op = 0
    while op != 6:
        print("Ingrese 1 para cargar Alumnos")
        print("Ingrese 2 para mostrar Alumnos")
        print("Ingrese 3 para mostrar Alumnos con promedio > 8")
        print("Ingrese 4 para ordenar Alumnos por legajo")
        print("Ingrese 5 para contar por nota")
        print("Ingrese 6 para Salir")
        op = int(input())

        if op == 1:
            cant = int(input("Ingrese la cantidad de alumnos: "))
            vec_alumnos = cargar_vector(cant)
        if op == 2:
            mostrar_vector(vec_alumnos)
        if op == 3:
            mostrar_vector_may8(vec_alumnos)
        if op == 4:
            ordenar_vector(vec_alumnos)
        if op == 5:
            vec_cont = contar_notas(vec_alumnos)
            for i in range(10):
                print("Cantidad de", i+1, ":", vec_cont[i])


if __name__ == '__main__':
    programa()

