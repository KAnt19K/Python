'''
1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''

my_file = open("file1.txt", "w")
my_line = input('Введите данные')

while my_line:
    my_file.writelines(my_line)
    my_line = input('Введите текст \n')
    if not my_line:
        break
my_file.close()

my_line = open("file1.txt", 'r')
content = my_line.readlines()
print(content)
my_line.close()
