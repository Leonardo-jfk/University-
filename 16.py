import random


def selection_sort():
    v = [random.randint(1,100) for _ in range(34)]
    # ordenamiento por seleccion direct
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

    print("pri",v)
    print(linear_search(v, 40))
    print(binary_search(v, 40))
    # print("sel",r)

def linear_search(v, x):
    # r = -1
    # for i in range(len(v)):
    #     if x == v[i]:
    #         r = i
    #
    # return r
    n = len(v)
    for i in range(n):
        if x == v[i]:
            return i
    else:
            return -1


def binary_search(v, x):
    # busqueda binaria... asume arreglo ordenado...
    # izq, der = 0, len(v) - 1
    # while izq <= der:
    #     c = (izq + der) // 2
    #     if x == v[c]:
    #         return c
    #     # else:
    #     #     return -1
    #
    #     if x < v[c]:
    #         der = c - 1
    #     else:
    #         izq = c + 1
    #
    # return -1

    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1


if __name__ == "__main__":
    selection_sort()