# объявление функции
def is_valid_password(password):
    pass_new = password.split(':')
    a, b, c = pass_new[0], int(pass_new[1]), int(pass_new[2])
    if len(pass_new) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
    return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))