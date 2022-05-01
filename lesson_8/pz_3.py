class OwnError(Exception):
    def __init__(self, num):
        self.num = num


num_list = []

while True:
    try:
        while True:
            el = input('Введите число (для остановки введите "q"): ')
            if el == 'q':
                break
            else:
                if el.isdigit():
                    num_list.append(int(el))
                elif el == el:
                    try:
                        num_list.append(float(el))
                    except ValueError:
                        print('Вы ввели не число')
                else:
                    raise OwnError('Вы ввели не число')
        print(num_list)

    except OwnError as err:
        print(err)
    else:
        break
