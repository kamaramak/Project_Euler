'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


ans = []
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if str(n) == str(n)[::-1]:
            ans.append(n)
print(*sorted(ans), sep='\n')
