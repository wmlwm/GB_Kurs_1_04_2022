class ComplexNumbers:

    def __init__(self, num_1, cmplx_1, num_2, cmplx_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.cmplx_1 = cmplx_1
        self.cmplx_2 = cmplx_2
        self.sum_1 = complex(self.num_1, self.cmplx_1)
        self.sum_2 = complex(self.num_2, self.cmplx_2)

    def __add__(self):  # сложение

        return f'Сложение: {(self.sum_1 + self.sum_2)}'

    def __mul__(self):  # умножение (x * y)
        return f'Умножение: {(self.sum_1 * self.sum_2)}'


cn = ComplexNumbers(3, 1, 2, 4)

print(cn.__add__())
print(cn.__mul__())
