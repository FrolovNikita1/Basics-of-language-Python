
my_list = [7, 5, 3, 3, 2]
data = []
menu = '1.Введите число\n2.Вывести Рейтинг - введите "stop" '

while True:

    print(menu)
    elm1 = input('Введите число: ')

    if elm1 != 'stop':

        sp1 = {
            'spisok': elm1,
        }
        my_list.append(int(elm1))

    else:
        print(sorted(my_list, reverse=True))

        break
