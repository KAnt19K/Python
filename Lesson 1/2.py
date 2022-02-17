number = int(input('Введите время в секундах'))
#print(number)

minuts = number // 60
#print(minuts)
second = number - (minuts * 60)
#print(second)
hour = minuts // 60
print('Ваше время', hour, ':', minuts, ':', second)
