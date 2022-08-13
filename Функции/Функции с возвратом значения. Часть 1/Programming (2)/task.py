# объявление функции
def get_factors(num):
    a=[]
    for i in range(1,num+1):
        if num%i==0:
            a.append(i)
    return a

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))