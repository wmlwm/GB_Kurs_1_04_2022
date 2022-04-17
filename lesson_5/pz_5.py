from my_func import el_num

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить её на экран.


with open('file5.txt', 'w', encoding='utf-8') as my_f:
    my_f.write('1 2 3 4 5 6 7 8 9')

with open('file5.txt', 'r', encoding='utf-8') as my_f:
    for el in my_f:
        print(sum(el_num(el)))
