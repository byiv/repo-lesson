# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = 'ДА' if is_police else 'НЕТ'

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поернула на {direction}')

    def show_speed(self):
        print(f'Скорость атомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость атомобиля {self.speed}'
              if self.speed < 60 else f'Скорость атомобиля {self.speed} превышает 60')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость атомобиля {self.speed}'
              if self.speed < 40 else f'Скорость атомобиля {self.speed} превышает 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(80, 'black', 'Audi')
work = WorkCar(50, 'blue', 'Ford')
police.show_speed()
print(police.is_police)
work.turn('Право')
print(work.is_police)
work.show_speed()
