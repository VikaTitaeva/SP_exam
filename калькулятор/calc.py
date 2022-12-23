choice = input('''
Выберите операцию:
+ сложение
- вычитание
* умножение
/ деление
^ возведение в степень
''')
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
 
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
 
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
 
elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
elif choice == '^':
    print('{} ^ {} = '.format(num_1, num_2))
    print(num_1 ** num_2)
 
else:
    print('Проверьте корректность данных.')