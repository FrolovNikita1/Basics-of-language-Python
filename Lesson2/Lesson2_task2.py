
num1 = int(input('Введите количество элементов в списке '))

result_list = []

while num1 > 0:
    elm1 = input('Введите элемент ')
    result_list.insert(0, elm1)
    num1 = num1 - 1
a = result_list

print('Было', result_list)

b = 0
for result_list in range(int(len(a) / 2)):
    a[b], a[b + 1] = a[b + 1], a[b]
    b += 2

print('Стало', a)
