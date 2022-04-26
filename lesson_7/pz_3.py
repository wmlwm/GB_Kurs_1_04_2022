class Cell:

    def __init__(self, n_cell, c_cell):
        self.n_cell = n_cell  # кол-во ячеек клетки
        self.c_cell = c_cell  # кол-во ячеек в ряду

    def __add__(self, other):  # сложение
        return f'Сложение: {(self.n_cell + other.n_cell)}'

    def __sub__(self, other):  # вычитание (x - y)
        if (self.n_cell - other.n_cell) > 0:
            return f'Вычитание: {(self.n_cell - other.n_cell)}'
        else:
            return f'Вычитание: результат меньше или равен 0'

    def __mul__(self, other):  # умножение (x * y)
        return f'Умножение: {(self.n_cell * other.n_cell)}'

    def __truediv__(self, other):  # деление (x / y)
        return f'Деление: {round((self.n_cell // other.n_cell), 2)}'

    def __mod__(self, other):  # остаток от деления (x % y)
        return f'{(self.n_cell % other.n_cell)}'

    @property
    def make_order(self):
        for i in range(0, (self.n_cell // self.c_cell)):
            print('*' * self.c_cell)
        return f'{"*" * (self.n_cell % self.c_cell)}'


c_1 = Cell(18, 5)
c_2 = Cell(12, 4)
c = Cell(22, 5)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)

print(f'{c.make_order}')
