n = int(input())
second = n % 10
while n > 9:
    num = n % 10
    n = n // 10
second = num
print(second)

