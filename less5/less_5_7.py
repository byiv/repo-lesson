# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open('less_5_7.txt') as my_file:
    content = my_file.readlines()
firm_list = []
firm_dict = {}
for el in content:
    firm_dict[el.split()[0]] = int(el.split()[2]) - int(el.split()[3])
firm_list.append(firm_dict)
average_profit = 0
for el in firm_dict.values():
    average_profit += el if el > 0 else 0
firm_list.append(dict({'average_profit': average_profit}))
with open('less_5_7.json', 'w') as my_file_json:
    json.dump(dict({'firm': firm_list}), my_file_json)
