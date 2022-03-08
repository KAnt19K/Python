'''
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, ' поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn_right(self):
        print(self.name, 'Повернула направо')

    def turn_left(self):
        print(self.name, 'Повернула налево')

    def show_speed(self):
        print('Скорость', self.name, 'составляет', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Скорость', self.name, 'составляет', self.speed, 'км/ч')
        if self.speed > 60:
            print(self.name, 'превысил (а) скорость на ', self.speed - 40, 'км/ч')
        else:
            print('Скорость', self.name, 'в норме')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Скорость', self.name, 'составляет', self.speed, 'км/ч')
        if self.speed > 40:
            print(self.name, 'превысил (а) скорость на ', self.speed - 40, 'км/ч')
        else:
            print('Скорость', self.name, 'в норме')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(120, 'Black', 'BMW', False)
bmw.turn_left()
bmw.show_speed()
smart = TownCar(70, 'Red', 'Smart', False)
smart.show_speed()
kia = WorkCar(39, 'White', 'Kia', False)
kia.turn_right()
kia.show_speed()
ford = PoliceCar(110, 'Blue', 'Ford', True)
ford.show_speed()
