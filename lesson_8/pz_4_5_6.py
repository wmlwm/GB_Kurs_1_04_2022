class Storehouse:
    def __init__(self):
        self.dict = {}

    def add_to(self, equipment):
        self.dict.setdefault(equipment.name, equipment.amount)


class Equipment(Storehouse):
    def __init__(self, name, amount):
        super().__init__()
        self.name = name
        self.amount = amount


class Printer(Equipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)


class Scanner(Equipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)


class Xerox(Equipment):
    def __init__(self, name, amount):
        super().__init__(name, amount)


s = Storehouse()
try:
    scanner = Scanner('Сканер', 2)
    if int(scanner.amount):
        s.add_to(scanner)
except ValueError:
    print('Введите кол-во сканеров в виде числа')

try:
    printer = Printer('Принтер', 1)
    if int(printer.amount):
        s.add_to(printer)
except ValueError:
    print('Введите кол-во принтеров в виде числа')

try:
    xerox = Xerox('Ксерокс', 3)
    if int(xerox.amount):
        s.add_to(xerox)
except ValueError:
    print('Введите кол-во ксероксов в виде числа')

print(s.dict)
