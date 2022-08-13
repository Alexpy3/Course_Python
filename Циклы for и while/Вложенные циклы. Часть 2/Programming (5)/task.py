n = int(input())
total_sum = 0
total_pro = 1
for i in range(1, n+1):
    total_pro *= i
    total_sum += total_pro
print(total_sum)