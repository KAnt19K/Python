'''
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
'''
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

my_file = open('file4.txt', 'r')
for i in my_file:
    i = i.split(' ', 1)
    new_file.append(my_dict[i[0]] + '  ' + i[1])
print(new_file)

my_file2 = open('file4_1.txt', 'w')
my_file2.writelines(new_file)
my_file2.close()


