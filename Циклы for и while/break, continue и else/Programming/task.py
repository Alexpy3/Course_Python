n = int(input())
# flag = True
for i in range(2, n+1):
    if n % i == 0:
        break
print(i)

