n, total = int(input()), 0
for i in range(1, 1+n):
    total += (-1)**(i+1)*i
print(total)
