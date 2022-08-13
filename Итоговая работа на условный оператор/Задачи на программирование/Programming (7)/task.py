x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 == x2 and (1 <= y2 <= 3 or 5 <= y2 <= 8)) or (y1 == y2 and (1 <= x2 <= 3 or 5 <= x2 <= 8)):
    print('YES')
elif (x1 - x2 == y1 - y2) or (x2 - x1 == y2 - y1) or (x1 - x2 == y2 - y1) or (x2 - x1 == y2 - y1):
    print('YES')
else:
    print('NO')
