import random
from clase import *

def validar(inf):
    n = int(input("Ingrese la cant de servicios(mayor a 0): "))
    while n <= inf:
        n = int(input("Se pidio mayor a 0. cargue de nuevo:"))
    return n

def cargar():
    n = validar(0)
    v = n * [None]
    nom = "Leo", "Lucas", "Feli", "Nico", "Mateo", "Gero"
    for i in range(n):
        codigo = random.randint(1, 1000)
        cliente = random.choice(nom)
        tipo = random.randint(1, 10)
        importe = random.randint(1000, 3000)
        v[i] = Servicio(codigo, cliente, tipo, importe)
        print(v[i])
    print("Arreglo cargado")
    return v

def mostrar(v):
    n = len(v)
    i1 = int(input("i1: "))
    i2 = int(input("i2: "))
    cs = 0

    for i in range(n-1):
        for k in range(i+1, n):
            if v[i].codigo > v[k].codigo:
                v[i], v[k] = v[k], v[i]
    for j in range(n):
        if i1 <= v[j].importe <= i2:
            cs += 1
            print(v[j])
    print("Cantidad de servicios mostrados: ", cs)

def contar(v):
    n = len(v)
    vc = 11 * [0]

    for i in range(n):
        pos = v[i].tipo
        vc[pos] += 1
    for k in range(10):
        if vc[k] > 0:
            print(f"Tipo:  {k +1} Cantidad:  {vc[k]}" )


def principal():
    v = []
    op = -1

    while op != 5:
        print("1) Cargar arreglo")
        print("2) Mostrar datos entre i1 e i2")
        print("3) Determinar cant de servicios de un tipo")
        print("4) Determinar si existe servicio con cleinte = num")
        print("5) Salir")
        op = int(input("Cargue la opcion:"))
        if op == 1:
            v = cargar()

        if op == 2:
            if v:
                mostrar(v)

            else:
                print("El vector no se cargó aún...")

        if op == 3:
            if v:
                contar(v)

            else:
                print("El vector no se cargó aún...")

        if op == 4:
            if v:
                pass

            else:
                print("El vector no se cargó aún...")

        elif op == 5:
            print("Saliendo...")
            break

if __name__ == "__main__":
    principal()