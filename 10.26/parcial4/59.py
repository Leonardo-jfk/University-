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
    titulos = ["aaaa", "harry", "hobbit", "lord of ", "game of", "star wars"]

    for art in range(n):
        codigo = random.randint(100, 999)
        titulo = random.choice(titulos)
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

def main():
    arreglo_fait = False
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
            # elif op == 3:
            #     buscar_titulo(p)
            # elif op == 4:
            #     buscar_codigo(p)
            # elif op == 5:
            #     conteo(p)
            # elif op == 6:
            #     crear_archivo(p)
            # elif op == 7:
            #     mostrar_archivo()
        else:
            print("l'opcion 1")


# script principal...
if __name__ == '__main__':
    main()