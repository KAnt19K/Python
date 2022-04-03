'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, my_dates):
        self.my_dates = str(my_dates)

    @classmethod
    def number(cls, my_dates):
        date_list = []
        for i in my_dates.split():
            if i != '-': date_list.append(i)
        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def examination(dd, mm, yyyy):
        if 1 <= mm <= 12:
            if 0 <= yyyy <= 2022:
                return ('Введено все верно')
            else:
                return ('Введен не существующий год')
        else:
            return ('Введен не существующий месяц')


today = Date('11 - 09 - 2021')
print(today)
print(Date.examination(11, 23, 2022))
print(today.examination(11, 11, 3011))
print(Date.number('11 - 09 - 2021'))
print(today.number('11 - 09 - 2021'))
print(Date.examination(1, 11, 2019))
