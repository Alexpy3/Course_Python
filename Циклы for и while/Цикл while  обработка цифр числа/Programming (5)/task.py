n = int(input())
last_num = n % 10
flag = True
while n != 0:
    num = n % 10
    if last_num != num:
        flag = False
    n = n // 10
if flag == True:
    print('YES')
else:
    print('NO')




