profit = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))

if profit > cost:
    print('Прибыль составила: ', profit - cost)
else:
    print('Убыток составил: ', cost - profit)
