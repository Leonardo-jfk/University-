import canvas
def opcion1():
    cx = float(input('Coordenada x: '))
    cy = float(input('Coordenada y: '))
    p = canvas.init(cx, cy)
    print(canvas.to_string(p))
def opcion2():
    cx = float(input('Coordenada x: '))
    cy = float(input('Coordenada y: '))
    p = canvas.init(cx, cy)
    d = canvas.distance(p)
    print('Distancia al origen:', d)
def opcion3():
    cx1 = float(input('Punto 1 - Coordenada x: '))
    cy1 = float(input('Punto 1 - Coordenada y: '))
    p1 = canvas.init(cx1, cy1)
    cx2 = float(input('Punto 2 - Coordenada x: '))
    cy2 = float(input('Punto 2 - Coordenada y: '))
    p2 = canvas.init(cx2, cy2)
    pd = canvas.gradient(p1, p2)
    if pd is not None:
        print('Pendiente de la recta que los une:', pd)
    else:
        print('Pendiente no definida (recta vertical)')
def menu():
    op = -1
    while op != 4:
        print('1. Cargar y mostrar un punto')
        print('2. Distancia al origen')
        print('3. Pendiente de la recta que une dos puntos')
        print('4. Salir')
        op = int(input('Ingrese opcion: '))
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
if __name__ == '__main__':
    menu()