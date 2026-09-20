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
    titulos1 = ("Fundación", "Imperio", "Planeta", "Horizonte", "Océano", "Cielo")
    titulos2 = ("Luz", "Oscuridad", "Felicidad", "Quietud", "Sabiduría", "Maldición")
    for i in range(n):
        cod = str(random.randint(10000, 50000))
        tit= random.choice(titulos1) + " y " + random.choice(titulos2) + " " + str(i+1)
        tip = random.randint(1, 30)
        cos = round(random.uniform(0, 20000), 2)
        v[i] = clase.Publicacion(cod, tit, tip, cos)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

    p = cp = ac = 0
    cos = float(input("Costo a filtrar (se mostrarán los registros cuyo costo sea mayor a este): "))
    print("Listado de publicaciones con costo mayor a", cos, ":" )
    for i in range(n):
        if v[i].costo > cos:
            cp += 1
            ac += v[i].costo
            print(v[i])
    if cp != 0:
        p = ac // cp
    print("Costo promedio de las publicaciones mostradas:", round(p, 2))
    print()


def contar(v):
    n = len(v)
    ct = 30 * [0]

    for i in range(n):
        # el tipo de publicacón viene entre 1 y 30... restar uno para compatibilizar con los índices del vector c...
        ind = v[i].tipo - 1
        ct[ind] += 1

    x = int(input("Cantidad a filtrar (se mostrarán los contadores con valor mayor a este): "))
    print("Cantidad de publicaciones por tipo:")
    for k in range(30):
        if ct[k] > x:
            # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de publicación:", k+1, "Cantidad:", ct[k])
    print()


def buscar(v):
    n = len(v)
    nom = input("Título de la publicacion a buscar: ")
    t = int(input("Tipo de la publicacion a buscar (número entre 1 y 30): "))
    for i in range(n):
        if nom == v[i].titulo and t == v[i].tipo:
            print("Encontrado:")
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
