item, day, count = [input() for _ in range(3)]

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
shop = {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.70, 'pineapple': 5.50, 'grapes': 3.85}
weekend_shop = {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60, 'kiwi': 3.00, 'pineapple': 5.60,'grapes': 4.20}

if not (day in days and item in shop.keys()):
    print('error')
else:
    if days.index(day) <= 4:
        print(f'{(shop[item] * float(count)):.2f}')
    else:
        print(f'{(weekend_shop[item] * float(count)):.2f}')

'''
grapefruit
Saturday
1.25
'''