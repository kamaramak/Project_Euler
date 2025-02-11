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