print('Задача №3')
print('-' * 15)

print('Вывод числа n в виде суммы чисел n + nn + nnn')

n = input('Введите число: ')

#sum_n = int(str(n)) + int(str(n + n)) + int(str(n + n + n))
sum_n = int(n) + int(n+n) + int(n+n+n)

print(f'{n} + {n + n} + {n + n + n} = ', sum_n)
