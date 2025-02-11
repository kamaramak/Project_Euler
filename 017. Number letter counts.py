'''If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


data = {0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'onethousand'}
ans = ''

for i in range(1, 1000):
    a = ''
    i1 = i % 10  # Последняя цифра
    i2 = (i - i1) % 100  # десятки
    i3 = (i - i2 - i1) // 100  # количество сотен
    a += data[i3]
    a = a + 'hundred' if i3 != 0 else a
    a = a + 'and' if i3 != 0 and i % 100 != 0 else a
    if i in data or 11 <= i % 100 <= 19:
        a += data[i % 100]
        print(i, a)
    else:
        a += data[i2]
        a += data[i1]
        print(i, a)
    ans += a
a = data[1000]
print(1000, a)
ans += a

print(ans)
print(len(ans))
