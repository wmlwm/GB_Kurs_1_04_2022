class Worker:

    def __init__(self, name, surname, position, wage, bonus, _income=None):
        if _income is None:
            _income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income

    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'


class Position(Worker):

    def get_r_p(self):
        return f'Full name: {self.name} {self.surname}\nPosition: {self.position}'

    def get_total_income(self):
        return sum(self.income.values())


p = Position('Igor', 'Petrov', 'Security', 15000, 5000)

print(f'{p.get_r_p()}\nIncome: {p.get_total_income()}')
