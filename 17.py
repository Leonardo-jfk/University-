# def read(leg, nom, pro):
#     n = len(leg)
#     for i in range(n):
#         leg[i] = int(input('Legajo: '))
#         nom[i] = input('Nombre: ')
#         pro[i] = float(input('Promedio: '))
#
#
# def procesar(leg, nom, pro):
#     im = 0
#     for i in range(1,len(pro)):
#         if pro[i] > pro[im]:
#             im = i
#     return leg[im], nom[im], pro[im]
#
#
# def test():
#     n = int(input('Cantidad de alumnos: '))
#     leg = n * [0]
#     nom = n * ['']
#     pro = n * [0.0]
#     read(leg, nom, pro)
#
#     r = procesar(leg, nom, pro)
#
#     print('Datos del estudiante pedido...')
#     print('Legajo:', r[0])
#     print('Nombre:', r[1])
#     print('Promedio:', r[2])
#
#
# if __name__ == '__main__':
#     test()
#
#
#
# def read(ventas):
#     n = len(ventas)
#     for i in range(n):
#         ventas[i] = int(input('Monto de venta[' + str(i) + ']: '))
#
#
# def sort(ventas):
#     n = len(ventas)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if ventas[i] < ventas[j]:
#                 ventas[i], ventas[j] = ventas[j], ventas[i]
#
#
# def display(ventas, cant):
#     n = len(ventas)
#     if cant > n:
#         print('La cantidad de ventas registradas no alcanza para el listado pedido...')
#         return
#
#     print('Montos de las', cant, 'ventas pedidas:')
#     for i in range(cant):
#         print('Monto[', i, ']:', ventas[i])
#
#
# def test():
#     n = int(input('Cantidad de ventas a cargar: '))
#     ventas = n * [0.0]
#     read(ventas)
#
#     sort(ventas)
#
#     print()
#     display(ventas, 3)
#
#
# if __name__ == '__main__':
#     test()

#
# def read(temp):
#     n = len(temp)
#     for i in range(n):
#         temp[i] = int(input('Temperatura[' + str(i) + ']: '))
#
#
# def amplitud(temp):
#     n = len(temp)
#     my = mn = temp[0]
#     for i in range(1, n):
#         if temp[i] > my:
#             my = temp[i]
#         elif temp[i] < mn:
#             mn = temp[i]
#
#     return my - mn
#
#
# def test():
#     n = int(input('Cantidad de temperaturas a cargar: '))
#     temp = n * [0.0]
#     read(temp)
#
#     d = amplitud(temp)
#
#     print('Amplitud térmica:', d)
#
#
# if __name__ == '__main__':
#     test()

#
# def read(leg, nom, pro):
#     n = len(leg)
#     for i in range(n):
#         leg[i] = int(input('Legajo: '))
#         nom[i] = input('Nombre: ')
#         pro[i] = float(input('Promedio: '))
#
#
# def search(nom, x):
#     n = len(nom)
#     for i in range(n):
#         if x == nom[i]:
#             return i
#     return -1
#
#
# def test():
#     n = int(input('Cantidad de alumnos: '))
#     leg = n * [0]
#     nom = n * ['']
#     pro = n * [0.0]
#     read(leg, nom, pro)
#
#     x = input('Ingrese el nombre del estudiante a buscar: ')
#     ind = search(nom, x)
#
#     if ind != -1:
#         print('El estudiante pedido está registrado en la posición', ind, 'y sus datos son:')
#         print('Legajo:', leg[ind])
#         print('Nombre:', nom[ind])
#         print('Promedio:', pro[ind])
#     else:
#         print('No hay un estudiante con ese nombre...')
#
#
# if __name__ == '__main__':
#     test()
#
# def contar():
#     n = 5
#     v = n * [0]
#
#     num = int(input('Ingrese un valor entre 0 y' + str(n) + '(con –1 corta):'))
#     while num != -1:
#         if 0 <= num < n:
#             v[num] += 1
#         else:
#             print('Error. El número debe ser >= 0 y <', n)
#         num = int(input('Ingrese otro valor entre 0 y' + str(n) + '(con –1 corta):'))
#
#     return print(v)
#
# if __name__ == '__main__':
#     contar()

def read(destinos, montos):
    n = len(destinos)
    for i in range(n):
        destinos[i] = int(input('Código de destino de la llamada (valor entre 0 y 24 por favor): '))
        montos[i] = float(input('Monto: '))


def process(destinos, montos):
    n = len(destinos)

    s = 25 * [0]
    for i in range(n):
        d = destinos[i]
        if 0 <= d <= 24:
            s[d] += montos[i]

    return s


def display(s):
    print('Listado solicitado de llamadas...')

    m = len(s)
    for i in range(m):
        if s[i] != 0:
            print('Destino:', i, 'Total:', s[i])


def test():
    n = int(input('Cantidad de llamadas: '))
    destinos = n * [0]
    montos = n * [0.0]
    read(destinos, montos)

    s = process(destinos, montos)

    # print()
    display(s)


if __name__ == '__main__':
    test()