print('Задача №1')
print('-' * 15)
print('Проверка типа элементов списка: \n')
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, '2', 'asd', (1, 'd'), {1, 'd', 44.4}]

print(f'Лист {my_list}')

for i in my_list:
    print(f'Элемент "{i}" имеет тип - {type(i)}')
