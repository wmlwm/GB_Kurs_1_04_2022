from abc import ABC, abstractmethod


class Garment(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Coat(Garment):

    @abstractmethod
    def get_v(self):
        pass


class Costume(Garment):

    @abstractmethod
    def get_h(self):
        pass


class Tailor(Coat, Costume):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_v(self):
        return round(self.v / 6.5 + 0.5, 2)

    def get_h(self):
        return round(2 * self.h + 0.3, 2)

    @property
    def my_method(self):
        return f"Параметры: H - {self.h}, V - {self.v}"


t = Tailor(25, 5)

print(t.my_method)
print(f'Для изготовления пальто потребуется {t.get_v()} м. ткани')
print(f'Для изготовления костюма потребуется {t.get_h()} м. ткани')
print(f'Общий расход ткани составит {round(t.get_h() + t.get_v(), 2)} м.')
