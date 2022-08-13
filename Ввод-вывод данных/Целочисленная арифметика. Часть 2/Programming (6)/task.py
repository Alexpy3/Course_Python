num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
Sum = digit1 + digit2 + digit3
Pro = digit1 * digit2 * digit3
print('Сумма цифр =', Sum)
print('Произведение цифр =', Pro)