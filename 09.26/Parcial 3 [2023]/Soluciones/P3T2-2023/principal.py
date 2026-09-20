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
    nombres = ("AJ", "BC", "ZE", "RT", "PL", "HS", "UB", "KW", "LM")
    for i in range(n):
        vu = random.choice(nombres) + str(i)
        ps = random.randint(1, 400)
        pa = random.randint(1, 20)
        at = random.randint(1, 200)
        im = round(random.uniform(0, 20000), 2)
        v[i] = clase.Ticket(vu, ps, pa, at, im)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].vuelo > v[j].vuelo:
                v[i], v[j] = v[j], v[i]

    num = int(input("Número de asiento (se mostrarán los tickets cuyo número de asiento sea mayor a este): "))
    print("Listado de tickets con número de asiento mayor a", num, ":")
    for i in range(n):
        if v[i].asiento > num:
            print(v[i])
    print()


def acumular(v):
    n = len(v)
    c = 20 * [0]

    for i in range(n):
        # el número de pais viene entre 1 y 20... restar uno para compatibilizar con los índices del vector c...
        ind = v[i].pais - 1
        c[ind] += v[i].importe

    t = int(input("Importe (se mostrarán los acumuladores mayores a este valor): "))
    print("Importes acumulados por país, mayores a", t, ":")
    for k in range(20):
        if c[k] > t:
            # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Pais destino:", k+1, "Importe acumulado:", round(c[k], 2))
    print()


def buscar(v):
    n = len(v)
    id = int(input("Número de identificación del pasajero a buscar: "))
    for i in range(n):
        if id == v[i].pasajero:
            print("Encontrado:")
            print("Número de asiento:", v[i].asiento, " - País destino:", v[i].pais)
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
        print("3. Acumular por pais")
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
                acumular(v)
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
