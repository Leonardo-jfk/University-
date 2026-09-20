import random
import clase


# carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def cargar():
    n = validar(0)
    v = n * [None]
    nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(n):
        exp = random.randint(1, 50000)
        nom1 = random.choice(apellidos)
        nom2 = random.choice(apellidos)
        car = nom1 + " vs " + nom2
        tj = random.randint(1, 15)
        nc = random.choice(nombres) + " " + nom1 + " " + random.choice(apellidos)
        im = round(random.uniform(0, 20000), 2)
        v[i] = clase.Juicio(exp, car, tj, nc, im)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].caratula > v[j].caratula:
                v[i], v[j] = v[j], v[i]

    cj = 0
    mon = float(input("Importe a filtrar (se mostrarán los juicios cuyo importe sea mayor a este): "))
    print("Listado de juicios con importe mayor a", mon, ":" )
    for i in range(n):
        if v[i].importe > mon:
            cj += 1
            print(v[i])
    print("Cantidad de juicios mostrados:", cj)
    print()


def contar(v):
    n = len(v)
    ct = 15 * [0]

    for i in range(n):
        # el tipo de juicio viene entre 1 y 15... restar uno para compatibilizar con los índices del vector c...
        ind = v[i].tipo - 1
        ct[ind] += 1

    c = int(input("Cantidad a filtrar (se mostrarán los contadores con valor mayor a este): "))
    print("Cantidad de juicios por tipo:")
    for k in range(15):
        if ct[k] > c:
            # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de juicio:", k+1, "Cantidad:", ct[k])
    print()


def buscar(v):
    n = len(v)
    cod = int(input("Número de expediente a buscar: "))
    for i in range(n):
        if cod == v[i].expediente:
            print("Encontrado - Datos actuales:")
            print(v[i])
            hon = float(input("Nuevo monto de honorarios a asignar: "))
            v[i].importe = round(hon, 2)
            print("Datos con el importe de honorarios actualizado:")
            print(v[i])
            print()
            return
    print("No estaba...")
    print()


def principal():
    v = []
    op = -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Contar por tipo")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 3:
            if v:
                contar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                buscar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
