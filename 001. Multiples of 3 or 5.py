'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

# ans = 0
# for i in range(1000):
#     ans = ans + i if i % 3 == 0 or i % 5 == 0 else ans
# print(ans)
print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))
