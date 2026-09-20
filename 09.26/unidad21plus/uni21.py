# p = []
# for i in range(3):
#     p.append([])
#     for j in range(2):
#         p[i].append([])
#         for k in range(4):
#             p[i][j].append([])
#
# p[2][1][3] = 'Prueba'
# print(p)
import random
#
# def test(mat):
#     fils = len(mat)
#     cols = len(mat[0])
#     for k in range(cols):
#         ac = 0
#         for g in range(fils):
#             ac += mat[k][g]
#         p = ac / fils
#         print('Indice:', k, '- Promedio:', p)
# #
# def registrar(a, c):
#     reg = []
#     for i in range(a):
#         reg.append([])
#         for j in range(c):
#             reg[i].append([])
#             reg[i][j] = 50
#
#     return reg


def test(mat):
    n = len(mat)
    m = len(mat[0])
    r = [n*[0] for k in range(m)]

    for i in range(n):
        for j in range(m):
            r[j][i] = mat[i][j]

    return r


def main():

    matriz = [[random.randint(1,100) for i in range(10)] for j in range(10)]
    # for i in range(20):
    #     print(matriz)
    # test(matriz)
    # registrar(20, 44)
    r = test(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])

    print()
    print("ggffffffffffff")
    for i in range(len(r)):
        for j in range(len(r[i])):
            print(r[i][j])

main()