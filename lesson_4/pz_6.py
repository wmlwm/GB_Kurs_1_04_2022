from itertools import count, cycle

print('Задача №6')
print('-' * 15)

# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

# count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

# cycle

my_list = ['around', 'the', 'world']
i = 1
for el in cycle(my_list):
    if i > 9:
        break
    print(el)
    i += 1
