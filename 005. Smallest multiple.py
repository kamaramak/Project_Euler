''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


def prime_factors(num):
    curr = 2
    answer = []
    if num == 2:
        return [2]
    while curr <= num:
        if num % curr == 0:
            answer.append(curr)
            num //= curr
            while num % curr == 0:
                answer.append(curr)
                num //= curr
        curr += 1
    return answer

def smallest_multiple(a, b):
    ans = 1
    data = {}
    for i in range(a, b + 1):
        factors = prime_factors(i)
        for factor in factors:
            tmp = data.setdefault(factor, 0)
            count_factor = factors.count(factor)
            if count_factor > tmp:
                data[factor] = count_factor
    for key, value in data.items():
        ans *= key ** value
    return ans

minimum = 1
maximum = 20
print(smallest_multiple(minimum, maximum))
