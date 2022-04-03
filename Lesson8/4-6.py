'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class OfficeEquipment:

    def __init__(self, name, price, quantity, number_list):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_list
        self.my_store_full = []
        self.my_store = []
        self.user = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def basket(self):
        try:
            my_name = input('Введите наименование')
            my_price = int(input('Введите стоимость за единицу'))
            my_quantity = int(input('Введите количество'))
            user_store = {'Модель устройства': my_name, 'Цена за ед': my_price, 'Количество': my_quantity}
            self.user.update(user_store)
            self.my_store.append(self.user)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        q = input('Для выхода - Q, продолжение - Enter')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.basket(self)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'Общее количество {self.numb} шт.'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'Общее количество {self.numb} шт.'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'Общее количество {self.numb} шт.'


a = Printer('hp', 1700, 3, 3)
b = Scanner('Canon', 3200, 5, 3)
c = Copier('Xerox', 1200, 1, 7)
print(a.basket())
print(b.basket())
print(c.basket())
print(a.to_print())
print(c.to_copier())
