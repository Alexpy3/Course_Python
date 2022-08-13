# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    while is_prime(num+1) == False:
        num+=1
        continue
    return num+1    

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))