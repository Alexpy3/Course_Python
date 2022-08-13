a,b,c = len(input()), len(input()), len(input())
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print('YES')
else:
    print('NO')
