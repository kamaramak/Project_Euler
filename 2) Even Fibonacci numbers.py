ans = 0
num1, num2 = 0, 1
while num2 <= 4 * 10 ** 6:
    num1, num2 = num2, num1 + num2
    ans = ans + num2 if num2 % 2 == 0 else ans
print(ans)
