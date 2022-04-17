import json

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в
# котором каждая строка будет содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
# Пипец

l_dict2 = []

with open('file7.txt', 'r', encoding='utf-8') as my_f:
    prof_dict = []
    for line in my_f:

        sp_line = line.split()
        profit = int(sp_line[2]) - int(sp_line[3])
        if profit > 0:
            prof = 'прибыль'
            prof_dict.append(profit)
        else:
            prof = 'убыток'
        print(f'{sp_line[1]} {sp_line[0]} - выручка: {sp_line[2]}, издержки: {sp_line[3]}, {prof}: {profit}')
    print(f'Средняя прибыль фирм: {sum(prof_dict) / len(prof_dict)}')

with open('file7.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        sp_line = line.split()
        l_dict2.append({sp_line[0]: int(sp_line[2]) - int(sp_line[3])})
    l_dict2.append({'avg_prof': sum(prof_dict) / len(prof_dict)})
    print(l_dict2)

with open('my_file.json', 'w', encoding='utf-8') as f_json:
    json.dump(l_dict2, f_json)
