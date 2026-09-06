# class Libro:
#     def __init__(self, cod, tit, aut):
#         self.isbn = cod
#         self.titulo = tit
#         self.autor = aut
#
#
# def test():
#     n = 10
#     lib = n * [None]
#     for i in range(n):
#         lib[i].cod = i
#     print('Terminado...')
#
#
#
# def main():
#     test()
# if __name__ == '__main__':
#     test()

#
# class Libro:
#     def __init__(self, cod, tit, aut):
#         self.isbn = cod
#         self.titulo = tit
#         self.autor = aut
#
#
# def test():
#     a = Libro(1, 'AAA', 'aaa')
#     b = Libro(2, 'BBB', 'bbb')
#     c = Libro(3, 'CCC', 'ccc')
#
#     n = 4
#     v = n * [None]
#     v[0] = a
#     v[1] = b
#     v[2] = c
#     v[3] = v[1]
#
#     a = None
#     b = None
#     c = None
#
#     for i in range(n-1):
#         v[i] = None
#
#     for i in range(n):
#         print(v[i])
#
#     print('Terminado...')
#
#
# if __name__ == '__main__':
#     test()


import random

class Insumo:
    def __init__(self, valor, cantidad):
        self.valor = valor
        self.cantidad = cantidad




def total_value(pieza):
    tv = 0
    for insumo in pieza:
        monto = insumo.valor * insumo.cantidad
        tv += monto
    return tv


def opcion3(pieza):
    print('Monto total en insumos para la pieza:', total_value(pieza))

def ordenar(pieza):
        n = len(pieza)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if pieza[i].valor > pieza[j].valor:
                    pieza[i], pieza[j] = pieza[j], pieza[i]

def main():
    n = 5
    pieza = n * [None]
    valor = [ random.randint(0, 100) for i in range(n)]
    cantidad = random.randint(0, 10)

    menuOption = int(input("1er: "))
    if menuOption == 1:
        for i in range(n):
            pieza[i] = Insumo(valor[i], cantidad)

            print(pieza[i])

    # total_value(pieza)
    opcion3(pieza)
    ordenar(pieza)

    for i in range(n):
        # print(Insumo[i].valor)
        print(pieza[i].valor)


if __name__ == '__main__':
    main()