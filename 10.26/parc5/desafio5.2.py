class Perceptron:
    def __init__(self, w0, w1, umbral, desc="P"):
        self.w0 = w0
        self.w1 = w1
        self.umbral = umbral
        self.descripcion = desc

    def __str__(self):
        r = f"Perceptrón: {self.descripcion} - (W0: {self.w0} - W2: {self.w1} - Umbral: {self.umbral})"
        return r

    def activar(self, x0, x1):
        s = self.w0 * x0 + self.w1 * x1
        if s > self.umbral:
            return 1
        return 0


# --- Funciones de procesamiento de resultados ---

def contar_salida_final_1(s):
    cont = 0
    for f in range(len(s)):
        if s[f][4] == 1:  # Salida del último perceptrón (P4)
            cont += 1
    return cont


def contar_todas_salidas_1(s):
    cont = 0
    for f in range(len(s)):
        for c in range(len(s[f])):
            if s[f][c] == 1:
                cont += 1
    return cont


def indice_primero_con_salida_1(s):
    for f in range(len(s)):
        for c in range(len(s[f])):
            if s[f][c] == 1:
                return c
    return None


def indice_ultima_entrada_todos_0(s):
    iue0 = None
    for f in range(len(s)):
        cont = 0
        for c in range(len(s[f])):
            if s[f][c] == 1:
                break  # Si hay un 1, la fila no nos sirve, cortamos
            cont += 1
        if cont == 5:
            iue0 = f  # Si contó 5 ceros, actualizamos la última fila encontrada
    return iue0


# --- Función Principal ---

def principal():
    entradas = [
        #  x0        x1
        [(0, 0), (0, 1)],
        [(1, 0), (1, 1)],
        [(1, 2), (2, 1)],
        [(0, 2), (2, 2)],
        [(2, 0), (2, 3)],
        [(3, 2), (0, 3)],
        [(3, 0), (3, 3)],
        [(2, 4), (4, 2)],
        [(4, 4), (0, 4)],
        [(4, 0), (1, 5)],
        [(5, 1), (5, 5)],
        [(0, 5), (5, 0)],
        [(6, 6), (4, 6)],
        [(2, 6), (6, 2)],
        [(7, 6), (7, 7)],
        [(2, 5), (3, 5)],
        [(5, 2), (5, 3)],
        [(3, 6), (0, 3)],
        [(1, 7), (2, 1)],
        [(0, 2), (3, 7)],
    ]

    # Creación de los 5 perceptrones
    p0 = Perceptron(1, 2, 1, "P0")
    p1 = Perceptron(1, 1, 2, "P1")
    p2 = Perceptron(3, 1, 3, "P2")
    p3 = Perceptron(2, 1, 3, "P3")
    p4 = Perceptron(1, 1, 1, "P4")

    p = [p0, p1, p2, p3, p4]

    # Matriz s de 20 filas y 5 columnas iniciada en ceros
    s = [[0] * 5 for _ in range(20)]

    # Ejecución de las 20 corridas de entrenamiento
    for f in range(20):
        # Desempaquetamos las tuplas correspondientes a x0 y x1
        x0_val0, x0_val1 = entradas[f][0][0], entradas[f][0][1]
        x1_val0, x1_val1 = entradas[f][1][0], entradas[f][1][1]
        
        # P0 toma los valores directos de x0
        s[f][0] = p[0].activar(x0_val0, x0_val1)
        
        # P1 toma los valores directos de x1
        s[f][1] = p[1].activar(x1_val0, x1_val1)
        
        # P2 toma como entrada las salidas de P0 y P1
        s[f][2] = p[2].activar(s[f][0], s[f][1])
        
        # P3 toma los valores directos de x1 (como se indica en el enunciado)
        s[f][3] = p[3].activar(x1_val0, x1_val1)
        
        # P4 toma como entrada las salidas de P2 y P3
        s[f][4] = p[4].activar(s[f][2], s[f][3])

    # Llamada a las funciones de cálculo
    r1 = contar_salida_final_1(s)
    r2 = contar_todas_salidas_1(s)
    r3 = indice_primero_con_salida_1(s)
    r4 = indice_ultima_entrada_todos_0(s)

    # Resultados en pantalla
    print("-" * 50)
    print("RESULTADOS DEL DESAFÍO 05:")
    print("-" * 50)
    print(f"r1.) Cantidad de veces con salida final 1: {r1}")
    print(f"r2.) Cantidad total de salidas 1 en la red: {r2}")
    print(f"r3.) Índice del primer perceptrón en dar 1: {r3}")
    print(f"r4.) Índice de la última fila con todos 0: {r4}")
    print("-" * 50)

if __name__ == '__main__':
    principal()