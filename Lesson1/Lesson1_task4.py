num1 = input('Введите целое число - ')
num2 = int(num1)
max1 = 1

while num2 != 0:
    num3 = (num2 % 10)

    if num3 > max1:
        max1 = num3

    num2 = (num2 // 10)

print(max1)
