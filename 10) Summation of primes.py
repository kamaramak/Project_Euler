import time

import numpy as np

"""Алгоритм 'Решето Эратосфена' улучшенное использованием numpy вектора"""
start = time.time()
n = 2000000
a = np.array(list(range(n + 1)), dtype='int64')
a[1] = 0
data = []
i = 2
while i <= n:
    if a[i] != 0:
        data.append(a[i])
        a[i::i] = 0
    i += 1
# print(*data, sep='\n')
print('Количество: ', len(data))
print('Сумма простых: ', np.sum(data))
finish = time.time()
print('С векторами нумпай', finish - start)
