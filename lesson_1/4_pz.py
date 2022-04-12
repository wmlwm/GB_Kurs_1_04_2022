print('Задача №4')
print('-' * 15)

print('Поиск самой большой цифры в числе')

number = int(input('Введите целое положительное число: '))

if number > 0 and number % 1 == 0:
    max_number = 0
    while number > 0:
        a = number % 10
        number //= 10
        if a > max_number:
            max_number = a
    print('Самая большая цифра в числе: ', max_number)

else:
    print('Введите целое положительное число')
