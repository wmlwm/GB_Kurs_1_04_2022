print('Задача №5')
print('-' * 15)

print('Считаем приыбль/убыток фирмы')

profit = int(input('Какая прибыль у фирмы?: $'))
costs = int(input('Какие издержки у фирмы?: $'))
result = profit - costs

if profit > costs:
    profitability = (result / profit) * 100
    print(f'Рентабельность составляет ${result:.2f} или {profitability:.2f}%')

    employees = int(input('Укажите количество сотрудников в фирме: '))
    profit_employess = result / employees
    print(f'На одного сотрудника приходится прибыль в размере ${profit_employess:.2f}')

elif profit < costs:

    print(f'Убыток составляет {result:.2f}$')

else:
    print('Прибыль равна издержкам')
