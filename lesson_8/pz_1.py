class Date:
    def __init__(self, date):
        self.d = date

    def __str__(self):
        return self.d

    def __call__(self, n_d):
        self.d = n_d

    @classmethod
    def date_cls(cls, int_d):
        int_d = int_d.d.split('-')
        return f'{[int(i) for i in int_d]}'

    @staticmethod
    def date_stat(val_d):
        val_d = val_d.d.split('-')
        if int(val_d[1]) in range(1, 13):
            return val_d
        else:
            return 'Указанный месяц на находится в диапазоне 1=12 '


dd = Date('01-05-2022')  # (input('Введите дату в формате dd-mm-yyyy: '))

print(dd.d)
print(Date.date_cls(dd))
print(Date.date_stat(dd))
