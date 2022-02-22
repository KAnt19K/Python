user_word = input('Введите несколько слов')
user_word = user_word.split()

for el in user_word:
    if len(el) <= 10:
        print(el)
    else:
        print(el[0:10])
