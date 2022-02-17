number = int(input('Введите целое положительное число'))

numbers = []
while number > 0:
    i = number % 10
    number = number // 10
    numbers.append(i)
    continue

result = max(numbers)
print(result)



