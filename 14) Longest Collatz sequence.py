def memo(f):
    data = {}
    def inner(*args, **kwargs):
        if args not in data:
            data[args] = f(*args, **kwargs)
        return data[args]
    return inner

@memo
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    if n % 2 == 1:
        return 1 + collatz(3 * n + 1)

print(max(range(1, 10**6), key=collatz))
