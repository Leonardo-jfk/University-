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


def contar_salida_final_1(s):
    cont = 0
    for f in range(len(s)):
        if s[f][4] == 1:
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
                break
            cont += 1
        if cont == 5:
            iue0 = f
    return iue0


def principal():
    entrada = [
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

    p0 = Perceptron(1, 2, 1, "P0")
    p1 = Perceptron(1, 1, 2, "P1")
    p2 = Perceptron(3, 1, 3, "P2")
    p3 = Perceptron(2, 1, 3, "P3")
    p4 = Perceptron(1, 1, 1, "P4")
    p = [p0, p1, p2, p3, p4]

    s = [[0] * 5 for _ in range(20)]

    for f in range(len(entrada)):
        x0 = entrada[f][0]
        x1 = entrada[f][1]
        s[f][0] = p[0].activar(x0[0], x0[1])
        s[f][1] = p[1].activar(x1[0], x1[1])
        s[f][2] = p[2].activar(s[f][0], s[f][1])
        s[f][3] = p[3].activar(x1[0], x1[1])
        s[f][4] = p[4].activar(s[f][2], s[f][3])

    for f in range(20):
        print(f, s[f])

    print("r1:", contar_salida_final_1(s))
    print("r2:", contar_todas_salidas_1(s))
    print("r3:", indice_primero_con_salida_1(s))
    print("r4:", indice_ultima_entrada_todos_0(s))


if __name__ == '__main__':
    principal()