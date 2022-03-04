'''
5. Создать (программно) текстовый файл, записать
в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''


def summary():
    try:
        with open('file5.txt', 'w+') as my_file:
            numbers = input('Введите числа через пробел \n')
            my_file.writelines(numbers)
            my_numbers = numbers.split()

        print(sum(map(int, my_numbers)))
    except ValueError:
        print('Вы не ввели числа')

summary()
