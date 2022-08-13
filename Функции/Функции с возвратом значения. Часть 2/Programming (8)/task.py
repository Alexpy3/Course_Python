# объявление функции
def convert_to_python_case(text):
    s = ''
    for i in text:
        if i.isupper():
            s += '_'
        s += i.lower()
    return s[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))