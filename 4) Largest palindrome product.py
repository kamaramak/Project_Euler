ans = []
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if str(n) == str(n)[::-1]:
            ans.append(n)
print(*sorted(ans), sep='\n')