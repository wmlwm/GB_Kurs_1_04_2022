# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

with open('file1.txt', 'w') as my_f:
    while True:
        in_str = (input(f'Введите данные в файл. Оставьте пустую строку для прекращения ввода: '))
        # sum_numb = None
        if in_str != '':
            my_f.writelines(f'{in_str}\n')
        else:
            break

with open('file1.txt', 'r') as my_f:
    while True:
        content = my_f.read()
        print(content)
        if not content:
            break
