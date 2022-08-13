a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a == c and (1 <= d <= 3 or 5 <= d <= 8)) or (b == d and (1 <= c <= 3 or 5 <= c <= 8)):
    print('YES')
else:
    print('NO')
