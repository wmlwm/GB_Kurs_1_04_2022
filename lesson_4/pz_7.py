from functools import reduce
from itertools import count

print('Задача №7')
print('-' * 15)


# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция вызывается следующим образом:
# for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!

def fact(n):
    def my_func(el1, el2):
        return el1 * el2

    my_list = [el for el in range(1, n + 1)]
    print(reduce(my_func, my_list))


fact(5)


# если честно я не понял зачем изобретать велосипед если функция
# реализованная в 5 задаче отлично подходит для подсчета факториала,
# и можно просто вложить одну функцию в другую,
# но раз надо сделать через yield то пусть будет через yield

def fact2(n):
    def my_func(el1, el2):
        return el1 * el2

    my_list = list(range(1, n + 1))
    yield reduce(my_func, my_list)


for el in fact2(5):
    print(el)

