''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_large(nums):
    a = nums[0]
    for i in range(len(nums) - 1):
        a = lcm(a, nums[i + 1])
    return a
print(lcm_large(list(range(1, 21))))
