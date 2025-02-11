import time

import numpy as np

"""Алгоритм 'Решето Эратосфена' улучшенное использованием numpy вектора"""
start = time.time()
n = 2 ** 30
a = np.array(list(range(n + 1)))
a[1] = 0
data = []
i = 2
while i <= n:
    if a[i] != 0:
        data.append(a[i])
        a[i::i] = 0
    i += 1
print(*data, sep='\n')
print(len(data))
finish = time.time()
print('С векторами нумпай', finish - start)

"""14.5799081325531 секунд при n = 10 ** 7"""

"""---------------------------------"""

# start = time.time()
# n = 10 ** 7
# a = list(range(n + 1))
# a[1] = 0
# data = []
# i = 2
# while i <= n:
#     if a[i] != 0:
#         data.append(a[i])
#         for j in range(i, n + 1, i):
#             a[j] = 0
#     i += 1
# print(*data, sep='\n')
# print(len(data))
# finish = time.time()
# print('Со списком обычным', finish - start)
# """30.91767454147339 секунд при n = 10 ** 7"""
