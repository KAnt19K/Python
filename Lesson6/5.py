'''
5. Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:  # канцелярская принадлежность
    def __init__(self, title):
        self.title = title

    def draw(self):  # отрисовка
        print('Запуск отрисовки')


class Pen(Stationery):  # ручка
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Для отрисовки выбрана', self.title)


class Pencil(Stationery):  # карандаш
    def __init__(self, title):
        super().__init__(title)

    def draw(self):  # отрисовка
        print('Это сообщение отрисовано', self.title)


class Handle(Stationery):  # маркер
    def __init__(self, title):
        super().__init__(title)

    def draw(self):  # отрисовка
        print('Сообщение отрисовано', self.title)


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()