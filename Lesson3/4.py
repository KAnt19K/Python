'''
4. Программа принимает действительное положительное
число x и целое отрицательное число y. Выполните
возведение числа x в степень y. Задание реализуйте
в виде функции my_func(x, y). При решении задания нужно
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''


def my_func(x, y):
    return x ** y


x = float(input('Введите положительное число'))
while True:
    if x < 0:
        print('Вы ввели отрицательное число')
        x = float(input('Введите положительное число'))
    continue

y = int(input('Введите отрицательное число'))
while True:
    if y > 0:
        print('Вы ввели положительное число')
        y = int(input('Введите отрицательное число'))
    continue

print(my_func(x, y))
