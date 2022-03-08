'''
1. Создать класс TrafficLight (светофор).

определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        if self.__color[0] == 'Red':
            print(self.__color[0])
        else:
            print('Загорелся неверный цвет')
        sleep(7)
        if self.__color[1] == 'Yellow':
            print(self.__color[1])
        else:
            print('Загорелся неверный цвет')
        sleep(2)
        if self.__color[2] == 'Green':
            print(self.__color[2])
        else:
            print('Загорелся неверный цвет')


traffic = TrafficLight()
traffic.running()


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


traffic = TrafficLight()
traffic.running()
