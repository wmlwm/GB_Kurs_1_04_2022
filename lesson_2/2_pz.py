print('Задача №2')
print('-' * 15)
print('"Кручу верчу запутать хочу" или обмен значениями элементов списка: \n')

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

count_el = int(input('Какое количество элементов вы хотите внести в список? \n'))

my_list = []

for i in range(count_el):
    i += 1
    f = input(f'Элемент #{i}: ')
    my_list.append(f)

print(f'Лист до изменения: {my_list}\n')

n_list = []

for i in range(len(my_list)):
    if i % 2 != 0:
        n_list.insert(i - 1, my_list[i])
    else:
        n_list.insert(i + 1, my_list[i])

print(f'Лист после изменения: {n_list}\n')

# -------------------------------------------------

print('-' * 55)
print('Вариант №2')
print('-' * 15)

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(f'Лист после изменения: {my_list}\n')

# -------------------------------------------------
print('-' * 55)
print('Вариант №3')
print('-' * 15)

my_str = ('weioutysdk')  # допустим пользователь ввел эту строку

my_list = []

for el in my_str:
    my_list.append(el)
print(my_list)
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
