a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b:
    print('Равнобедренный')
elif b == c:
    print('Равнобедренный')
elif a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
