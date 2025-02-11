import time
start = time.time()
num = 1
i = 2
a = []
while len(a) < 500:
    a = []
    num += i
    for j in range(1, int(num ** 0.5) + 1):
        if num % j == 0:
            a.extend([j, num // j])
            continue
    i += 1
print(num)
print(len(a))
finish = time.time()
print(finish - start)