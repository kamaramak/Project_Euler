'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


def largest_palindrom():
    ans = 0
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            prod = num1 * num2
            if str(prod) == str(prod)[::-1]:
                if prod > ans:
                    ans = prod
    return ans

print(largest_palindrom())
