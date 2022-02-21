my_list = [7, 5, 3, 3, 2]
user_rating = int(input('Введите рейтинг от 1 до 10'))

for el in range(len(my_list)):
    if my_list[el] == user_rating:
        my_list.insert(el + 1, user_rating)
        break
    elif my_list[0] < user_rating:
        my_list.insert(0, user_rating)
    elif my_list[-1] > user_rating:
        my_list.append(user_rating)
    elif my_list[el] > user_rating and my_list[el + 1] < user_rating:
        my_list.insert(el + 1, user_rating)
    print(my_list)
    user_rating = int(input("Введите число "))

print(my_list)
