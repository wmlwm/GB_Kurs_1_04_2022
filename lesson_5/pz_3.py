from my_func import el_num

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет
# оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.

with open('file3.txt', 'r', encoding='utf-8') as my_f:
    num_str = sum(1 for line in my_f)
    with open('file3.txt', 'r', encoding='utf-8') as my_f:
        print('Сотрудники с окладом меньше 20000: ')
        num = []
        for line in my_f:
            line = line.split()
            for i in line:
                if i <= '20000':
                    print(line)
            f = sum(float(s) for s in line if '0' <= s <= '999999999')
            num.append(f)
        sum_f = round(sum(num), 2)
        print(f'Средний оклад всех сотрудников {sum_f / num_str}')

# 2 вариант======================================

with open('file3.txt', 'r', encoding='utf-8') as my_f:
    num_str = sum(1 for line in my_f)

    with open('file3.txt', 'r', encoding='utf-8') as my_f:
        print('Сотрудники с окладом меньше 20000: ')
        num = []
        i = 0
        for line in my_f:

            el = el_num(line)
            el = float(f'{el[0]}.{el[1]}')
            if el <= 20000:
                num.append(el)
                print(line, end='')
                i += 1
        print('\n')
        print(f'Средний оклад таких сотрудников {round((sum(num)) / i, 2)}')

with open('file3.txt', 'r', encoding='utf-8') as my_f:
    num = []
    for line in my_f:
        el = (el_num(line, str, '.'))
        num.append(float((f'{el[0][1:]}{el[1]}')))
    print(f'Средний оклад всех сотрудников {round((sum(num) / num_str), 2)}')
