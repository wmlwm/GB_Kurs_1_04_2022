class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')


Pen('"картина"').draw()
Pencil('"скетч"').draw()
Handle('"плакат"').draw()