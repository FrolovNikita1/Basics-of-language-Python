dist1 = int(input('Введите результат забега в 1-й день - '))
dist2 = int(input('Введите желаемый результат - '))

dayX = 1

while dist2 > dist1:

    dist1 = (dist1 * 1.1)
    dayX = dayX + 1

print('Желаемый результат на - ', int(dayX), 'день')
