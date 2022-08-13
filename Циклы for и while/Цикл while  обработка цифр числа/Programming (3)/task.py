n = int(input())
total, total_sum = 0, 0
total_pro = 1
last = n % 10
while n != 0:
    digit = n % 10       # после цикла буде равно первому числу
    total_sum += digit
    total += 1
    total_pro *= digit
    a = total_sum / total
    Sum_digit = digit + last
    n = n // 10
print(total_sum, total, total_pro, a, digit, Sum_digit, sep='\n')




