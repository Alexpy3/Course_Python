n = int(input())
a = n // 100  # 1 число
b = n // 10 % 10  # 2 число
c = n % 10  # 3 число
if max(a, b, c) - min(a, b, c) == (a + b + c) - (max(a, b, c) + min(a, b, c)):
    print('Число интересное')
else:
    print('Число неинтересное')
