# Desarrollar un programa que permita manejar puntos en un plano. Por cada punto se
# deben indicar sus coordenadas (que pueden ser números en coma flotante) y una cadena de
# caracteres a modo de descriptor del punto cuando se muestren sus valores en pantalla. Incluir un
# menú de opciones que permita:
# 1. Cargar por teclado los datos de un punto y mostrar esos datos en pantalla.
# 2. Cargar por teclado los datos de un punto, y mostrar la distancia al origen desde ese punto.
# 3. Cargar por teclado los datos de dos puntos, y mostrar la pendiente de la recta que los une.



import canvas


def get_points():

    response = -1
    while response != 0:
        print("Menu options: ")
        print("1) Give us coordinates:")
        print("2) Show coordinates: ")

        print("0) End program ")
        response = int(input('Introduce un numero entero: '))

        if response == 1:
            coordinateX = float(input("Enter coordinate for X : "))
            coordinateY = float(input("Enter coordinate for Y : "))

        if response == 2:
            show = canvas.Point(coordinateX, coordinateY)
            return show


def main():

    get_points()



if __name__ == '__main__':
    main()