'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143'''


def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

print(primfacs(600851475143))
