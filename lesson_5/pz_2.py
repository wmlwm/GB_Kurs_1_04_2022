# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('file2.dat', 'r') as my_f:
    print(f'Кол-во строк: {sum(1 for line in my_f)}')

with open('file2.dat', 'r') as my_f:
    i = 0
    for line in my_f:
        i += 1
        print(f'Кол-во символов в {i}-й строке: {len(line) - 1}')

with open('file2.dat', 'r') as my_f:
    i = 0
    for line in my_f:
        i += 1
        print(f'Кол-во слов в {i}-й строке: {len(line.split())}')
