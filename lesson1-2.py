sec = int(input('введите время в секундах: '))

min = sec // 60
hour = min // 60
min = min % 60
sec = sec % 60

print(str(hour) + ':' + str(min) + ':' + str(sec))