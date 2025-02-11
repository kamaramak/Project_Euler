# ans = 0
# for i in range(1000):
#     ans = ans + i if i % 3 == 0 or i % 5 == 0 else ans
# print(ans)
print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))