'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class Division:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def division_null(number_1, number_2):
        try:
            return (number_1/number_2)
        except ZeroDivisionError:
            return ('В знаменателе ввели ноль')


my_del = Division(10,5)
print(Division.division_null(10, 5))
print(Division.division_null(10, 0))

