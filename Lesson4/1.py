'''
1. Реализовать скрипт, в котором должна быть предусмотрена
 функция расчёта заработной платы сотрудника. Используйте
 в нём формулу: (выработка в часах*ставка в час) + премия.
 Во время выполнения расчёта для конкретных значений необходимо
 запускать скрипт с параметрами.
'''
from sys import argv

time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = time * salary + bonus
    print('Зарплата сотрудника составила', result)
except ValueError:
    print('Вы не ввели цифры')


def my_func():
    try:
        time = int(input('Введите количество отработанных часов'))
        salary = int(input('Введите стоимость одного часа'))
        bonus = int(input('Введите сумму премии'))
        result = time * salary + bonus
        print('Зарплата сотрудника составила', result)
    except ValueError:
        print('Вы не ввели цифры')

my_func()