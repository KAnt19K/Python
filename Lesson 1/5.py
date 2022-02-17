profit = int(input('Введите вашу прибыль'))
costs = int(input('Введите ваши издержки'))
result = profit - costs

if result > 0:
    print('Вы сработали хорошо, ваша прибыль', result)
else:
    print('Вы сработали неочень хорошо, ваши издержки', result)

