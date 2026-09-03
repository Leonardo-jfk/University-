# Desarrollar un programa que permita manejar puntos en un plano. Por cada punto se
# deben indicar sus coordenadas (que pueden ser números en coma flotante) y una cadena de
# caracteres a modo de descriptor del punto cuando se muestren sus valores en pantalla. Incluir un
# menú de opciones que permita:
# 1. Cargar por teclado los datos de un punto y mostrar esos datos en pantalla.
# 2. Cargar por teclado los datos de un punto, y mostrar la distancia al origen desde ese punto.
# 3. Cargar por teclado los datos de dos puntos, y mostrar la pendiente de la recta que los une.

from tkinter import *

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, x, y):
        canvas.create_line(self.x, self.y, x, y)

def face(canvas):
    x, y, ancho, alto = 100, 100, 50, 50

def render():
        # configuracion inicial de la ventana principal...
        root = Tk()
        root.title('Cuestionario')

        # calculo de resolucion en pixels de la pantalla...
        maxw = root.winfo_screenwidth()
        maxh = root.winfo_screenheight()

        # ajuste de las dimensiones y coordenadas de arranque de la ventana...
        root.geometry("%dx%d+%d+%d" % (500, 500, 0, 0))

        # un lienzo de dibujo dentro de la ventana...
        canvas = Canvas(root, bg='white', width=maxw, height=maxh)
        canvas.grid(column=0, row=0)

        # desarrollar la gráfica...
        face(canvas)

        # lanzar el ciclo principal de control de eventos de la ventana...
        root.mainloop()

        point = Coordinate(100, 100)
        point2 = Coordinate(face(canvas(100, 100))



if __name__ == '__main__':
    render()
