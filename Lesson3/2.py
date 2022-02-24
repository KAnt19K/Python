'''
2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.
'''


def my_func(name, surname, year, city, malito, tel):
    return name, surname, year, city, malito, tel


name = input('Введите имя')
surname = input('Введите фамилию')
year = input('Введите год рождения')
city = input('Введите город проживания')
malito = input('Введите e-mail')
tel = input('Введите телефон')

print(my_func(name, surname, year, city, malito, tel))
