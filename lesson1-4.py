a = int(input('введите целое положительное число: '))
max = a % 10
b = a // 10

while b > 0:
    if b % 10 > max:
        max = b % 10
    b = b // 10

print (max)