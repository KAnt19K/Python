'''
5. Программа запрашивает у пользователя строку чисел,
 разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
 Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''


def my_func():
    while True:
        my_str = input('Введите числа через пробел. Для выхода напишите Q').split()
        if 'Q' in  my_str:
            break
        else:
            for el in my_str:
                el = int(el)
                my_list.append(el)
                result = sum(my_list)
            print(result)
        continue
    print('Ваша итоговая сумма', result)


my_list = []
my_func()
