# # Pre-orden: Mensajes en orden descendente (5, 4, 3, 2, 1)
# def mostrar_preorden(n):
#     if n > 0:
#         print(f"Mensaje {n}")
#         mostrar_preorden(n - 1)
#
# # Post-orden: Mensajes en orden ascendente (1, 2, 3, 4, 5)
# def mostrar_postorden(n):
#     if n > 0:
#         mostrar_postorden(n - 1)
#         print(f"Mensaje {n}", end="--")
#
# mostrar_preorden(5)
# # Salida:
# # Mensaje 5
# # Mensaje 4
# # Mensaje 3
# # Mensaje 2
# # Mensaje 1
#
# mostrar_postorden(5)
# # Salida:
# # Mensaje 1
# # Mensaje 2
# # Mensaje 3
# # Mensaje 4
# # Mensaje 5







# def menu():
#     print('1. Opcion 1')
#     print('2. Opcion 2')
#     print('3. Salir')
#     op = int(input('Ingrese opcion: '))
#     if op == 1:
#         print('Eligio la opcion 1...')
#     elif op == 2:
#         print('Eligio la opcion 2...')
#     elif op == 3:
#         return
#     menu()
#
#
# # script principal...
# menu()

def producto(a, b):
    if a == 0 or b == 0:
        return 0
    return a + producto(a, b-1)

print(producto(3, 5))