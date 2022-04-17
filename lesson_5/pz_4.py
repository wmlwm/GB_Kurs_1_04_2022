# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.


with open('file4.txt', 'r', encoding='utf-8') as my_f:
    with open('file4_translate.txt', 'w', encoding='utf-8') as new_f:
        for line in my_f:
            for old_str, new_str in ('One', 'Один'), ('Two', 'Два'), ('Three', 'Три'):
                line = line.replace(old_str, new_str)
            new_f.write(line)
with open('file4_translate.txt', 'r', encoding='utf-8') as new_f:
    for line in new_f:
        print(line, end='')
