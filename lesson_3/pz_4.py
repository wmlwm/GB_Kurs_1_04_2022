print('Задача №4')
print('-' * 15)

# 4. Программа принимает действительное положительное число x и целое отрицательное
# число y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.

print('1. Возведение в минусовую степень с помощью оператора **')


def my_func(x, y):
    try:
        if y > 0:
            y = y * -1
        return print(abs(x) ** y)
    except ZeroDivisionError:
        return


my_func(2, 3)


print('2. Возведение в минусовую степень без оператора **, с помощью цикла')


def my_func(x, y):
    try:
        if y > 0:
            y = y * -1
        i = 0
        a = 1
        while i < abs(y):
            i += 1
            a *= x

        return print(1 / a)
    except ZeroDivisionError:
        return


my_func(2, -3)
