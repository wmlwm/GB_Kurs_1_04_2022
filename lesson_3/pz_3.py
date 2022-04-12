print('Задача №3')
print('-' * 15)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

print('1. Решение, если функция принимает только три аргумента')


def my_func(var_1, var_2, var_3):
    a = [var_1, var_2, var_3]
    a.remove(min(a))
    print(sum(a))


my_func(4, 2, 3)

print('-' * 15)
print('2. Решение, если функция принимает множество аргументов, *через сортировку*')


def my_func2(*args):
    b = list(args)
    b.sort()
    b.reverse()
    return print(sum([b[0], b[1]]))


my_func2(7, 8, 4, 1, 2, 3)

print('-' * 15)
print('3. Решение, если функция принимает множество аргументов, *через while, min*')


def my_func3(*args):
    args = list(args)
    while len(args) > 2:
        args.remove(min(args))

    return print(sum(args))


my_func3(1, 2, 3, 4, 5)
my_func3(9, 1, 2, 3, 4, 5, 6, 7)

print('-' * 15)
print('4. Решение, если функция принимает множество аргументов, *через while, max*')


def my_func4(*args):
    args = list(args)
    el = []
    while len(el) < 2:
        el.append(args.pop(args.index(max(args))))

    return print(sum(el))


my_func4(9, 1, 2, 3, 4, 5, 6, 11)
