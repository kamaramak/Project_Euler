import time
start = time.time()
ans = []
flag = False
for a in range(1, 1000):
    if flag:
        break
    for b in range(1, 1000):
        c = 1000 - a - b
        if a + b + c == 1000 and a * a + b * b == c * c:
            print(a, b, c)
            print(a * b * c)
            flag = True
            break
finish = time.time()
print(finish - start)