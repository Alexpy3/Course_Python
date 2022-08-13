col1, col2 = input(), input()
if (col1 == 'красный' and col2 == 'синий') or (col1 == 'синий' and col2 == 'красный'):
    print('фиолетовый')
elif col1 == 'красный' and col2 == 'красный':
    print('красный')
elif (col1 == 'красный' and col2 == 'желтый') or (col1 == 'желтый' and col2 == 'красный'):
    print('оранжевый')
elif col1 == 'желтый' and col2 == 'желтый':
    print('желтый')
elif (col1 == 'синий' and col2 == 'желтый') or (col1 == 'желтый' and col2 == 'синий'):
    print('зеленый')
elif col1 == 'синий' and col2 == 'синий':
    print('синий')
else:
    print('ошибка цвета')