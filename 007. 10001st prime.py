'''By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10_001st prime number?'''


import time


start = time.time()
def prime_factors(num):
    curr = 3
    answer = []
    while curr <= num:
        if num % curr == 0:
            answer.append(curr)
            num //= curr
            while num % curr == 0:
                answer.append(curr)
                num //= curr
        curr += 2
    return answer

ans = 2
n = 3
count = 0
while count != 10000:
    if len(prime_factors(n)) == 1:
        ans = n
        count += 1
    n += 2
print(ans)
print(time.time() - start)
