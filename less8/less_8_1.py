# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, date):
        self.extract_data(date)

    @classmethod
    def extract_data(cls, date):
        try:
            date_list = [int(el) for el in date.split('-')]
            print(date_list)
        except ValueError:
            return print('Не верный формат даты (dd-nn-yyyy)')
        return cls.validation_data(date_list)

    @staticmethod
    def validation_data(date):
        print('Все верно!'
              if date[0] in range(1, 32) and date[1] in range(1, 13)
              else 'Не верный формат даты (dd-nn-yyyy)')


data = Data('32-12-2021')
