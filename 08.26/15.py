# n = 20
# v = n * [0]
# for i in range(n):
#     v[i] = 3*i



# n = 6
# v = n * [0]
# for i in range(n):
#     v[i] = '123'
#

# n = 6
# v = n * [0]
# for i in range(n+1):
#     v[i] = i
# print(v)

# v = [2, 4, 1, 6]
# v[0] = v[v[0]] * 3
# print('v[0]:', v[0])


# n = 5
# a = n * [0]
# for i in range(n):
#     a[i] = i + 1
#
# v = n * [0]
# for i in range(n):
#     v[a[i]] = a[i]
#
# print(v)



# def test():
#     n = 10
#     v = n * [0]
#
#     for i in range(n):
#         v[i] = int(input('v[' + str(i) + ']: '))
#
#     im = 0
#     for i in range(1, n):
#         if v[i] < v[im]:
#             im = i
#
#     print('El valor pedido es:', v[im])
#
#
# if __name__ == '__main__':
#     test()


def generar(v):
    n = len(v)

    ac = 0
    for i in range(n):
        ac += v[i]
    p = ac / n

    c = 0
    for i in range(n):
        if v[i] >= p:
            c += 1

    mp = c * [0]
    idx = 0
    for i in range(n):
        if v[i] >= p:
            mp[idx] = v[i]
            idx += 1

    return mp

generar([1, 3, 4, 5])