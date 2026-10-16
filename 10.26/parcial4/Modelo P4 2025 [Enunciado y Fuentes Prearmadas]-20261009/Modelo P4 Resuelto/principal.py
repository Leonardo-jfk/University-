import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clases
from clase import Pokemon


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Genera con datos aleatorios un objeto de la clase Pokemon y lo retorna.
def generar_aleatorio():
    NOMBRES = (
        "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
        "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill",
        "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
        "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
        "Sandshrew", "Sandslash", "Nidorino", "Nidorina", "Nidoqueen",
        "Nidorina", "Nidorino", "Nidoking", "Clefairy", "Clefable",
        "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat",
        "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect"
    )

    nombre = random.choice(NOMBRES)
    pokedex = random.randint(1, 1_025)
    tipo = random.randint(1, 18)
    puntos = random.randint(1, 5_550)
    evolucion = random.randint(1, 6)
    return Pokemon(nombre, pokedex, tipo, puntos, evolucion)


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def mostrar_archivo(fd):
    t = int(input("Tipo a promediar: "))
    ac = c = 0
    tam = os.path.getsize(fd)
    a = open(fd, "rb")
    while a.tell() < tam:
        poke = pickle.load(a)
        print(poke)
        if poke.tipo == t:
            ac += poke.pc
            c += 1
    a.close()
    if c != 0:
        prom = ac // c
    else:
        prom = 0
    print("Promedio pedido:", prom)


def grabar(v, fd):
    a = open(fd, "wb")
    for poke in v:
        if poke.pc <= 1500:
            pickle.dump(poke, a)
    a.close()


def contar(v):
    m = [[0] * 6 for f in range(18)]
    for poke in v:
        f = poke.tipo - 1
        c = poke.nivel - 1
        m[f][c] += 1

    for f in range(18):
        for c in range(6):
            if m[f][c] > 0:
                print("Tipo", f+1, "Nivel", c+1, ":", m[f][c])


def mostrar(v):
    t1 = int(input("Valor t1: "))
    t2 = int(input("Valor t2: "))
    t3 = int(input("Valor t3: "))
    c = 0
    for poke in v:
        print(poke)
        if poke.tipo in (t1, t2, t3):
            c += 1
    print("Cantidad de pokes de los tipos pedidos:", c)


def add_in_order(v, poke):
    n = len(v)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].numero == poke.numero:
            pos = c
            break
        elif v[c].numero > poke.numero:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [poke]


def cargar():
    n = validar(0)
    v = []
    for i in range(n):
        poke = generar_aleatorio()
        add_in_order(v, poke)
    return v


# Función principal o de arranque.
def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                contar(v)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                grabar(v, fd)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            if os.path.exists(fd):
                mostrar_archivo(fd)
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
