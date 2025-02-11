'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


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
