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
    nombres = ("Oficinista", "Mecánico", "Jardinero", "Programador", "Maestro")
    for i in range(n):
        id = random.randint(1, 25000)
        de = random.choice(nombres) + " " + str(i)
        ti = random.randint(0, 39)
        im = round(random.uniform(0, 20000), 2)
        v[i] = clase.Empleo(id, de, ti, im)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]

    print("Listado de empleos...")
    ac = 0
    for i in range(n):
        ac += v[i].importe
        print(v[i])
    print("Suma de todos los sueldos pagados:", ac)
    print()


def contar(v):
    n = len(v)
    c = 40 * [0]

    for i in range(n):
        # ind = v[i].tipo
        # c[ind] += 1
        c[v[i].tipo] += 1

    print("Cantidad de empleos por tipo...")
    for k in range(40):
        if c[k] != 0:
            print("Tipo:", k, "Cantidad:", c[k])
    print()


def buscar(v):
    n = len(v)
    num = int(input("Número de identificación del empleo a buscar: "))
    for i in range(n):
        if num == v[i].identificador:
            print("Encontrado:")
            print("Descripción del empleo:", v[i].descripcion, " - Sueldo:", v[i].importe)
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
        print("3. Conteo por tipo")
        print("4. BUscar")
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
