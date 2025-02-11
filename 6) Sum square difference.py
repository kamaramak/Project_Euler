import operator as op
data = list(range(1, 101))
data_first = list(map(lambda x: x * x, data))
print(sum(data) ** 2 - sum(data_first))