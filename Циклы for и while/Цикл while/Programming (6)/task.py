num = int(input())
total = 0
while num >= 25:
    total += 1
    num = num-25
while num >= 10:
    total += 1
    num = num-10
while num >= 5:
    total += 1
    num = num-5
while num >= 1:
    total += 1
    num = num-1
print(total)