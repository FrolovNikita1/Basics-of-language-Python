time = input('Введите секунды - ')
num1 = int(time)
num2 = (num1 % 60)
num3 = (num1 // 60) % 60
num4 = (num1 // 60) // 60

print(f'{num4}:{num3}:{num2}')






