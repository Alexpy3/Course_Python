n = int(input())
max1 = 0
min1 = 9
while n != 0:
    last_digit = n % 10
    if last_digit > max1:
        max1 = last_digit
    if last_digit < min1:
        min1 = last_digit
    n = n // 10
print('Максимальная цифра равна', max1)
print('Минимальная цифра равна', min1)

