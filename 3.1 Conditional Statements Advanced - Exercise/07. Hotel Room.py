month, nights = input(), int(input())

dis_st, dis_ap = 0, 0

dict_month = {
    'May': {'Studio': 50, 'Apartment': 65},
    'October': {'Studio': 50, 'Apartment': 65},
    'June': {'Studio': 75.20, 'Apartment': 68.7},
    'September': {'Studio': 75.20, 'Apartment': 68.7},
    'July': {'Studio': 76, 'Apartment': 77},
    'August': {'Studio': 76, 'Apartment': 77},
}

match nights:
    case _ if 7 < nights <= 14 and month in ['May', 'October']:
        dis_st = 0.95
    case _ if nights > 14 and month in ['May', 'October']:
        dis_st = 0.70
    case _ if nights > 14 and month in ['June', 'September']:
        dis_st = 0.80

if nights > 14:
    dis_ap = 0.90

price_ap = dict_month[month]['Apartment']
price_st = dict_month[month]['Studio']

if dis_ap > 0:
    price_ap *= dis_ap
if dis_st > 0:
    price_st *= dis_st

print(f'Apartment: {price_ap * nights:.2f} lv.')
print(f'Studio: {price_st * nights:.2f} lv.')

'''
May
15

# output:
Apartment: 877.50 lv.
Studio: 525.00 lv.
'''
