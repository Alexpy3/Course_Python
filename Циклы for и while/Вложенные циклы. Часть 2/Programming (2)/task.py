a, b = int(input()), int(input())
count = 0    # счетчик для конечного присваивания суммы
largest = 0  # число у которого сумма делителей больше
for i in range(a, b+1):
    total = 0
    for j in range(1, i+1):
        if i % j == 0:
            total += j
        if total >= count and i >= largest:
            count = total
            largest = i
print(largest, count)

