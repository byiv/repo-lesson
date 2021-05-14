# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes:
    @abstractmethod
    def print_info(self):
        print('Расчета суммарного расхода ткани!')


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        super().__init__()

    def print_info(self):
        print('Пожив одежды!')

    @property
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        super().__init__()

    def print_info(self):
        print('Пожив одежды!')

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


costume = Costume(170)
coat = Coat(42)
coat.print_info()
print(costume.fabric_consumption)
print(coat.fabric_consumption)
