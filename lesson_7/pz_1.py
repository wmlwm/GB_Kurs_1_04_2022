from itertools import zip_longest


class Matrix:

    def __init__(self, matrix_1, matrix_2, matrix_3):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.matrix_3 = matrix_3

    # def __add__(self, other):
    #     return Matrix(self.matrix_1 + other.matrix_1, self.matrix_2 + other.matrix_2, self.matrix_3 + other.matrix_3)
    def __add__(self, l_1, l_2, l_3):
        return [x + y + z for x, y, z in zip_longest(l_1, l_2, l_3, fillvalue=0)]

    def __str__(self):
        return f"Объект с параметрами ({self.matrix_1}, {self.matrix_2}, {self.matrix_3})"


def num_l(my_list, key=max):
    return my_list.index(key(my_list, key=len))


matx_1 = [[31, 22], [37, 43], [51, 86]]
matx_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matx_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

m_list = [matx_1, matx_2, matx_3]

el_l_num = len(m_list[num_l(m_list)]) - len(m_list[num_l(m_list, min)])
m_list[num_l(m_list, min)] = m_list[num_l(m_list, min)] + [[0]] * el_l_num

m = Matrix(m_list[0], m_list[1], m_list[2])

new_mat = []

for i in range(len(m_list)):
    new_mat.append(m.__add__(m.matrix_1[i], m.matrix_2[i], m.matrix_3[i]))
    # print(m.__add__(m.matrix_1[i], m.matrix_2[i], m.matrix_3[i]))

print(new_mat)
