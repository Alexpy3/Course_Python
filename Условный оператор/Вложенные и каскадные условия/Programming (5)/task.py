x, y, z = int(input()), int(input()), input()
if z == '+':
    print(x+y)
elif z == '-':
    print(x-y)
elif z == '*':
    print(x*y)
elif z == "/":
    if y != 0:
        print(x/y)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
