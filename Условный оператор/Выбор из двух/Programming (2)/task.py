n = int(input())
a = n // 1000      # 1 число
b = n // 100 % 10  # 2 число
c = n // 10 % 10   # 3 число
d = n % 10         # 4 число
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')