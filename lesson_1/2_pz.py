print('Задача №2')
print('-' * 15)

print('Перевод времени в секундах, в формат чч:мм:сс')

time_in_seconds = int(input('Введите время в секундах: '))

hours = time_in_seconds // 3600

minutes = (time_in_seconds // 60) - (time_in_seconds // 3600 * 60)

sec = (time_in_seconds % 3600) - (minutes * 60)

print(f'Время в формате чч:мм:сс будет: {hours:02}:{minutes:02}:{sec:02}')
