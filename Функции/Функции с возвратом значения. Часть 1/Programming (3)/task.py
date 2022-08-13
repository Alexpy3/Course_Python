# объявление функции
def number_of_factors(num):
    return len(get_factors(n))

def get_factors(num):
    a = []
    for i in range(1, num + 1):
        if num % i == 0:
            a.append(i)
    return a

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))