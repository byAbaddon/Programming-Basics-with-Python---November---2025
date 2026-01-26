budget, season = float(input()), input()
des, place = '', ''

if budget <= 100:
    des = 'Bulgaria'
    if season == 'summer':
        budget *= 0.30
        place = 'Camp'
    if season == 'winter':
        budget *= 0.70
        place = 'Hotel'
elif budget <= 1000:
    des = 'Balkans'
    if season == 'summer':
        budget *= 0.40
        place = 'Camp'
    if season == 'winter':
        budget *= 0.80
        place = 'Hotel'
else:
    des = 'Europe'
    place = 'Hotel'
    budget *= 0.90

print(f'Somewhere in {des}\n{place} - {budget:.2f}')

'''
1500
summer
'''
