import random


def merge(a, b):
    # crear el tercer arreglo con lugar para n + m elementos...
    n, m = len(a), len(b)
    t = n + m
    c = t * [0]
    # aplicar proceso de fusión...
    i = k = j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    # determinar cuál de los vectores (a o b) terminó primero...
    # ... apuntar con v al otro...
    v, pos = b,  j
    if i < n:
        v, pos = a, i
    # copiar en el vector de salida todos los valores que
    # quedaban en el vector v...
    while pos < len(v):
        c[k] = v[pos]
        pos += 1
        k += 1
    # retornar el vector fusionado...
    print(c)
    return c


def main():
    a = [random.randint(1, 100) for i in range(1, 10)]
    b = [random.randint(1, 100) for i in range(1, 10)]
    merge(a, b)
    # print(c)


if __name__ == '__main__':
    main()