from functools import reduce

print('Задача №5')
print('-' * 15)


# 5. Реализовать формирование списка, используя функцию range() и
# возможности генератора. В список должны войти чётные числа от 100 до 1000
# (включая границы). Нужно получить результат вычисления произведения всех
# элементов списка.

def my_func(el1, el2):
    return el1 * el2


my_list = [el for el in range(100, 1001, 2)]
print(reduce(my_func, my_list))
