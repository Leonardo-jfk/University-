def count(codigos):
    vc = 10 * [0]
    for d in codigos:
        vc[d] += 1

    print('Cantidad de socios en cada deporte disponible:')
    for i in range(10):
        if vc[i] != 0:
            print('Codigo de deporte:', i, 'Cantidad de socios registrados:', vc[i])



# def display(patentes, cabinas, x):
#     exists = False
#     print('Listado de vehiculos que pasaron por la cabina', x, ':')
#     for i in range(len(cabinas)):
#         if cabinas[i] == x:
#             exists = True
#             print('Patente:', patentes[i])
#
#     if not exists:
#         print('No se registraron vehiculos que hayan pasado por esa cabina')


def display(patentes, cabinas, x):
    print('Listado de vehiculos que pasaron por la cabina', x, ':')
    for i in range(len(cabinas)):
        if cabinas[i] == x:
            print('Patente:', patentes[i])

def main():
    codigos = [9, 3, 3, 2,8 ,4, 5]

    count(codigos)

    cabinas = [5, 23,1 ,21]
    display(codigos, codigos, 58)




    cad = 'Hola mundo otra vez'
    r = cad.find('un')
    print('Posición:', r)

    v = ['Hola', 'mundo', 'otra', 'vez']
    r = '*-*'.join(v)
    print(r)
main()
