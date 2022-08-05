profit = int(input('Введите прибыль: '))
revenue = int(input('Введите выручку: '))

print ('Рентабельность компании', profit / revenue * 100, '%')

emp_num = int(input('Введите число сотрудников: '))

print('Прибыль фирмы в расчёте на одного сотрудника: ', profit / emp_num)
