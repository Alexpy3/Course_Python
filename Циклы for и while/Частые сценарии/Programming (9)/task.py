total = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        total += 1
if total == 10:
    print('YES')
else:
    print('NO')

#иначе: "нет" и сразу выход
#в конце если счетчик = 10 пишем "ДА"