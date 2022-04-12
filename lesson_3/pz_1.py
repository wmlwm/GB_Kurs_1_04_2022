print('Задача №1')
print('-' * 15)


# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации
# деления на ноль.


def div():
    try:
        div_d = int(input('Деление чисел:\n введите делимое: '))
        div_r = int(input('Деление чисел:\n введите делитель: '))
    except ValueError:
        return
    try:
        div_d = div_d / div_r
        return div_d
    except ZeroDivisionError:
        return


print(f'Ответ: {div()}')
