month = int(input('Введите порядковый номер месяца, например: январь - 1'))

season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1 : 'winter', 2 : 'spring', 3: 'summer', 4: 'autumn'}

if month == 1 or month == 2 or month == 12:
    print(season_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(season_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(season_dict[3])
else:
    print(season_dict[4])

