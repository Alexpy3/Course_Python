# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        for j in range(i):
            if i + j <= base:
                print(fill, end='')

        print()

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)