m = int(input('Введите месяц в виде целого числа от 1 до 12 '))

year = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
        9: 'september', 10: 'october', 11: 'november',
        12: 'december'}
a = year[m]

seasons = {'january':'Winter', 'february':'Winter', 'december':'Winter',
           'march':'Spring', 'april':'Spring', 'may':'Spring',
           'june':'Summer', 'july':'Summer', 'august':'Summer',
           'september':'Autumn','october':'Autumn', 'november':'Autumn'}

print(seasons.get(a,))
