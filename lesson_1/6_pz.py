print('Задача №6')
print('-' * 15)
print('"RUN Вася RUN" или считаем сколько дней потребуется спортсмену, '
      'что бы улучшить свою результативность: ')

first_day_km = 2
last_day_km = 3
up_in_day = 0.1
days = 1

while True:
    print(f'{days}-й день: {first_day_km:.2f} км.')
    first_day_km = first_day_km + (first_day_km * up_in_day)
    if first_day_km > (last_day_km + (last_day_km * up_in_day)):
        break
    else:
        days += 1
    continue

print(f'Спортсмену потребуется {days} дней для достижения поставленной цели в {last_day_km} км.')
