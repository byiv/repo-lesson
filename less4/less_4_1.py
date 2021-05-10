# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения
# расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv


def payroll(arg):
    try:
        arg = [int(el) for el in arg if el.isdigit()]
        working_out, rate, prize = arg
        return (working_out * rate) + prize
    except ValueError:
        print('Не верные параметры. Введите параметры в формате: '
              'less_4_1.py working_out rate prize, '
              'где: '
              'working_out - выработка в часах; '
              'rate - ставка в час; '
              'prize - премия. '
              'Пример: '
              'less_4_1.py 168 1500 5000')


print(payroll(argv))
