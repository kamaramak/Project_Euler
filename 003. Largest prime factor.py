'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143'''


def largest_prime_factor(num):
    curr = 3
    answer = []
    if num == 2:
        return 2
    while curr <= num:
        if num % curr == 0:
            answer.append(curr)
            num //= curr
        curr += 2
    return answer[-1]

print(largest_prime_factor(600851475143))
