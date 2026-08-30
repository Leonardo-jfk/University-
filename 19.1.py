# class Fecha:
#     pass
#
# f = Fecha()
# f.day = 27
# f.month = 7
# f.year = 2015
#
# print('Fecha registrada: ', f.day, '/', f.month, '/', f.year, sep='')
#
#
# class Libro:
#     pass
#
# lib1 = Libro()
# lib1.codigo = 2345
# lib1.titulo = 'El Aleph'
#
# lib2 = Libro()
# lib2.codigo = 1267
# lib2.titulo = 'Rayuela'
# lib2.autor = 'Julio Cortázar'
#
# lib3 = Libro()
# lib3.isbn = 123456767
# lib3.nombre = 'El Tunel'
# lib3.precio = 145.56
#
# print(Libro)
#
#
#
#
#
# class Libro:
#     pass
#
#
# def init(cod, nom, aut):
#     libro = Libro()
#     libro.codigo = cod
#     libro.titulo = nom
#     libro.autor = aut
#     return libro
#
#
# def write(libro):
#     print('Datos del libro:')
#     print('Código:', libro.codigo, ' - Título:', libro.titulo, ' - Autor:', libro.autor)
#
#
# def test():
#     lib1 = init(2345, 'El Aleph', 'Jorge Luis Borges')
#     lib2 = init(1267, 'Rayuela', 'Julio Cortázar')
#     lib3 = init(1928, 'El Túnel', 'Ernesto Sábato')
#
#     write(lib1)
#     write(lib2)
#     write(lib3)
#
#
# if __name__ == '__main__':
#     test()

# class Libro:
#     pass
#
#
# def init(libro, cod, nom, aut):
#     # libro = Libro()
#     libro.codigo = cod
#     libro.titulo = nom
#     libro.autor = aut
#
#
# def write(libro):
#     print('Datos del libro:')
#     print('Código:', libro.codigo, ' - Título:', libro.titulo, ' - Autor:', libro.autor)
#
#
# def test():
#     lib1 = Libro()
#     init(lib1, 2345, 'El Aleph', 'Jorge Luis Borges')
#
#     lib2 = Libro()
#     init(lib2, 1267, 'Rayuela', 'Julio Cortázar')
#
#     lib3 = Libro()
#     init(lib3, 1928, 'El Túnel', 'Ernesto Sábato')
#
#     write(lib1)
#     write(lib2)
#     write(lib3)
#
#
# if __name__ == '__main__':
#     test()
#

#
#
# class Libro:
#     pass
#
#
# def init(libro, cod, nom, aut):
#     libro.codigo = cod
#     libro.titulo = nom
#     libro.autor = aut
#
#
# def write(libro):
#     print('Datos del libro:')
#     print('Código:', libro.codigo, ' - Título:', libro.titulo, ' - Autor:', libro.autor)
#
#
# def test():
#
#     lib1 = Libro()
#     init(lib1, 2345, 'El Aleph', 'Jorge Luis Borges')
#
#     lib2 = Libro()
#     init(lib2, 1267, 'Rayuela', 'Julio Cortázar')
#
#     lib3 = Libro()
#     init(lib3, 1928, 'El Túnel', 'Ernesto Sábato')
#
#     write(lib1)
#     write(lib2)
#     write(lib3)
#
#     # lib4 = lib2
#     # lib4.autor = 'Adolfo Bioy Casares'
#     #
#     lib4 = Libro()
#     init(lib4, lib2.codigo, lib2.titulo, lib2.autor)
#     lib4.autor = 'Adolfo ggBioy Casares'
#     lib2.autor = "hitler"
#
#     write(lib2)
#     write(lib4)
#
# if __name__ == '__main__':
#     test()

# class Estudiante:
#     def __init__(self, leg, nom, prom):
#         self.legajo = leg
#         self.nombre = nom
#         self.promedio = prom
#
#     def __str__(self):
#         r = ''
#         r += '{:<15}'.format('Legajo: ' + str(self.legajo))
#         r += '{:^90}'.format('Nombre: ' + self.nombre)
#         r += '{:>18}'.format('Promedio: ' + str(self.promedio))
#         return r
#
# print(Estudiante("555", "leo", "10"))
#


class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc

    def gradient(self, p2):
        dy = p2.y - self.y
        dx = p2.x - self.x

        if dx != 0:
            return dy / dx

        return None

def main():
    p = Point(2, 5)
    q = Point(4, 6)
    pd = p.gradient(q)
    print(pd)

main()