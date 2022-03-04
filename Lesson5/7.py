'''
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json

bisnes = {}
bisnes_dict = {}
bisnes_list = [bisnes]
profit_all = 0
profit_aver = 0
i = 0

with open('file7.txt', 'r') as my_file:
    for line in my_file:
        name, ownership, revenue, costs = line.split()
        bisnes[name] = int(revenue) - int(costs)
        if bisnes[name] >= 0:
            profit_all = profit_all + bisnes[name]
            i += 1
    if i != 0:
        profit_aver = profit_all / i
        print('Средняя прибыль равна', profit_aver)
    else:
        print('Прибыль отсутсвтует')

bisnes_dict = {'Средняя прибыль': round(profit_aver)}
bisnes.update(bisnes_dict)
print('Прибыль каждой компании', bisnes_list)

with open('file7.json', 'w') as my_file_js:
    json.dump(bisnes_list, my_file_js)

    js_str = json.dumps(bisnes_list)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
