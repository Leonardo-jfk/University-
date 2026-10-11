import pickle
import os.path
import random

class Articulo:
    def __init__(self, tit, cod, pg, tp, id):

        self.titulo = tit
        self.codigo = cod
        self.paginas = pg
        self.tipo = tp
        self.idioma = id
    def __str__(self):
        r = ''
        r += '{:<30}'.format('Titulo: ' + self.titulo)
        r += '{:<20}'.format('Codigo: ' + str(self.codigo))
        r += '{:<20}'.format('Paginas: ' + str(self.paginas))
        r += '{:<20}'.format('Tipo: ' + str(self.tipo))
        r += '{:<20}'.format('Idioma: ' + str(self.idioma))
        return r


def cargar_arreglo_ordenado():
    vector = []
    n = int(input("cant de articulos: "))
    titulos = ["aaaa", "harry", "hobbit", "lord of", "game of", "star wars"]
    titulosHelp = ["Holms", "Duman", "Lupin", "Napoleon"]

    for art in range(n):
        codigo = random.randint(100, 999)
        titulo = random.choice(titulos) + random.choice(titulosHelp)
        paginas = random.randint(1, 99)
        tipo = random.randint(0, 9)
        idioma = random.randint(0, 5)

#         alfabéticamente de acuerdo al título de los artículos.
        duplicate = False
        izq = 0
        der = len(vector)
        centro = (izq + der) // 2
        while izq < der:


            centro = (izq + der)//2
            if vector[centro].titulo > titulo:
                der = centro
            elif vector[centro].titulo < titulo:
                izq = centro + 1
            else:

                duplicate = True
                break

        if not duplicate:
            vector[izq:izq] = [Articulo(titulo, codigo, paginas, tipo, idioma)]

    return vector



def mostrar_arreglo(vector):
    cant = len(vector)

    for art in range(cant):
        print(vector[art])




def buscar_titulo(vector, iteamToCkeck):

    cant = len(vector)
    x = input("Ingrese el nombre a buscar: ")

    for i in range(cant):
        if str(getattr(vector[i], iteamToCkeck)) == x:
            return print(vector[i])


    print("ce n'existe pas")

def conteo(vector):
    cant = len(vector)
    cant_tipo = 10
    cant_idioma = 6

    # la cantidad de artículos por tipo e idioma
    arreglo_cantador = [[0 for i in range(cant_idioma)] for j in range(cant_tipo)]

    for i in range(10):
        print(arreglo_cantador[i])

    # for tipo in range(10):
    #     for idioma in range(5):
    #         if vector[tipo].idioma == idioma:
    #             arreglo_cantador[idioma][tipo] += 1
    for articulo in vector:
        arreglo_cantador[articulo.tipo][articulo.idioma] += 1


    for i in range(10):
        print(arreglo_cantador[i])

    return arreglo_cantador


def crear_archivo(vector, nameOfFile):
    cant = len(vector)
    file = open(nameOfFile, "wb")
    for i in range(cant):
        if vector[i].paginas > 10:
            pickle.dump(vector[i], file)


    file.close()


def mostrar_archivo(nameOfFile):

    file = open(nameOfFile, "rb")

    while file.tell() < os.path.getsize(nameOfFile):
        print(pickle.load(file))

    file.close()

def main():
    arreglo_fait, iteamToCkeck = False, ""
    nameOfFile = 'articulos.edi'
    vector = []
    op = -1
    while op != 0:
        print('Editorial UTN')
        print(' 1. Registrar articulos ordenados por título')
        print(' 2. Listado completo de articulos')
        print(' 3. Buscar un articulo por título')
        print(' 4. Buscar un articulo por código')
        print(' 5. Conteo por tipo e idioma')
        print(' 6. Crear archivo desde el arreglo (por cantidad de páginas)')
        print(' 7. Mostrar el archivo')
        print(' 8. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            vector = cargar_arreglo_ordenado()
            arreglo_fait = True
        if arreglo_fait:
            if op == 2:
                mostrar_arreglo(vector)
            elif op == 3:
                iteamToCkeck = "titulo"
                buscar_titulo(vector, iteamToCkeck)
            elif op == 4:
                iteamToCkeck = "codigo"
                buscar_titulo(vector, iteamToCkeck)
            elif op == 5:
                arreglo_cantador = conteo(vector)
            elif op == 6:
                nameOfFile = "acrivo.dat"
                crear_archivo(vector, nameOfFile)
            elif op == 7:
                mostrar_archivo(nameOfFile)
        else:
            print("l'opcion 1")


# script principal...
if __name__ == '__main__':
    main()