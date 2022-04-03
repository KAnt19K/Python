'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt

number_1 = input('Введите числитель')
number_2 = input('Введите знаменатель')

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    result = number_1/number_2
    print(result)
except ZeroDivisionError:
    print('В знаменателе ввели ноль')
except ValueError:
    print('В одном из частных введено не число')
