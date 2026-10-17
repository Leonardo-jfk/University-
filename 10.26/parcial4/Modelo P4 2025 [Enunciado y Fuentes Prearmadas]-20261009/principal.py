import os.path
import pickle
import random
# from multiprocessing.reduction import duplicate

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
    numero = random.randint(1, 1_025)
    tipo = random.randint(1, 18)
    puntos = random.randint(1, 5_550)
    evolucion = random.randint(1, 6)
    return Pokemon(nombre, numero, tipo, puntos, evolucion)


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n

def cargar_arreglo(v):

    der = len(v)
    v.clear()
    izq, duplicado, primer = 0, False, True
    n = validar(0)
    for i in range(n):
        pokemon = generar_aleatorio()

        der = len(v)
        izq = 0
        duplicado = False
        # centro = (izq + der) // 2
        # if primer:
        #     v.append(pokemon)
        #     primer = False
        while izq < der:
            centro = (izq + der) // 2
            if v[centro].numero > pokemon.numero:
                der = centro
            elif v[centro].numero < pokemon.numero:
                izq = centro + 1

            else:
                duplicado = True
                izq = centro
                break
        # if not duplicado:
        v[izq:izq] = [pokemon]



def mostrar_arreglo(v):
    for pokemon in v:
        print(pokemon)


def find_type(v):
    tipos_a_encontrar = []
    tipos_a_encontrar.append( int(input("alguno de tres tipos específicos t1")))
    tipos_a_encontrar.append( int(input("alguno de tres tipos específicos t2")))
    tipos_a_encontrar.append( int(input("alguno de tres tipos específicos t3")))



    contador = 0
    for pokemon in v:
        # for i in range(3):
        #     if pokemon.tipo == tipos_a_encontrar[i]:
        #         contador += 1
        if pokemon.tipo in tipos_a_encontrar:
            contador += 1

    return contador

def matriz_de_conteo(v):
    matriz = [[0] * 6 for i in range(18)]
    tipo = 0
    nivel = 0
    for pokemon in v:
        tipo = pokemon.tipo - 1
        nivel = pokemon.nivel - 1
        matriz[tipo][nivel] += 1

    return matriz


def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in range(filas):
        for columna in range(columnas):
            cantidad = matriz[fila][columna]
            if  cantidad > 0:
                print(f"La cantidad de pokens de tipo: {fila + 1} y nivel: {columna + 1} es:", cantidad)




def crear_archivo(v, fd):
    # cant = len(v)
    file = open(fd, "wb")

    for pokemon in v:
        if pokemon.pc < 1500:
            pickle.dump(pokemon, file)




    file.close()

def mostrar_archivo(fd):
    file = open(fd, "rb")
    t = int(input("tipo t que debe ser ingresado por teclado: "))
    endOfFile = os.path.getsize(fd)
    promedio, contador_puntos, cant = 0, 0, 0

    while file.tell() < endOfFile:

        pokemon = pickle.load(file)
        print(pokemon)
        if pokemon.tipo == t:

            contador_puntos += pokemon.pc
            cant += 1
    if cant > 0:
        promedio = contador_puntos / cant
    else:
        print("no tenemos de este PC")

    print("el promedio de puntos de combate: ", promedio)
    file.close()




# Función principal o de arranque.
def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            cargar_arreglo(v)

        elif op == 2:
            if v:
                mostrar_arreglo(v)
                print("eran de alguno de tres tipos específicos t1, t2 y t3: ", find_type(v))
            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                matriz = matriz_de_conteo(v)
                mostrar_matriz(matriz)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                crear_archivo(v, fd)
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
