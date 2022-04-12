if __name__ == "__main__":
    print('Задача №6')
    print('-' * 15)


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.


def int_func(*args):
    args = str(args)
    if args.islower() and args.isascii():
        print(args.title())
    else:
        print('Введите слово только из латинских букв в нижнем регистре')


if __name__ == "__main__":
    int_func('leonid', 'dima', 'vova')
