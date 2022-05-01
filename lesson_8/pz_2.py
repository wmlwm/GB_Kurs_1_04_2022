class OwnError(Exception):
    def __init__(self, num):
        self.num = num


print('Произведем деление')
inp_num_1 = input('Введите делимое: ')
inp_num_2 = input('Введите делитель: ')
try:
    inp_num_1 = int(inp_num_1)
    inp_num_2 = int(inp_num_2)
    if inp_num_1 == 0 or inp_num_2 == 0:
        raise OwnError('Вы ввели "0"! При делении "0" на любое число получается "0"')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(f'В результате деления получаем: {inp_num_1 / inp_num_2}')
