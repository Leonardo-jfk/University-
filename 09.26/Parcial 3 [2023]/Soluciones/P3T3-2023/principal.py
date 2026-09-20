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
        id = random.randint(1, 50000)
        nc = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        ts = random.randint(1, 10)
        im = round(random.uniform(0, 20000), 2)
        v[i] = clase.Servicio(id, nc, ts, im)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

    cs = 0
    i1 = int(input("Primer importe a filtrar: "))
    i2 = int(input("Segundo importe a filtrar: "))
    print("Listado de servicios con importe entre", i1, "y", i2, ":" )
    for i in range(n):
        if i1 <= v[i].importe <= i2:
            cs += 1
            print(v[i])
    print("Cantidad de servicios mostrados:", cs)
    print()


def contar(v):
    n = len(v)
    c = 10 * [0]

    for i in range(n):
        # el tipo de servicio viene entre 1 y 10... restar uno para compatibilizar con los índices del vector c...
        ind = v[i].tipo - 1
        c[ind] += 1

    print("Cantidad de servicios por tipo:")
    for k in range(10):
        if c[k] > 0:
            # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de servicio:", k+1, "Cantidad:", c[k])
    print()


def buscar(v):
    n = len(v)
    nom = input("Nombre del cliente a buscar: ")
    for i in range(n):
        if nom == v[i].nombre:
            print("Encontrado - Datos actuales:")
            print(v[i])
            v[i].importe += 2000
            print("Datos con el importe actualizado:")
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
