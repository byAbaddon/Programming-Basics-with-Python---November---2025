budget, season, fishers = float(input()), input(), int(input())

dict_seasons = {'Summer': 4200, 'Autumn': 4200, 'Spring': 3000, 'Winter': 2600}
price = dict_seasons[season]

match fishers:
    case _ if fishers <= 6:
        price *= 0.90
    case _ if 7 <= fishers <= 11:
        price *= 0.85
    case _ if fishers >= 12:
        price *= 0.75

if not fishers & 1 and not season == 'Autumn':
    price *= 0.95

money = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {money:.2f} leva left.')
else:
    print(f'Not enough money! You need {money:.2f} leva.')

'''
3000
Summer
11
'''
