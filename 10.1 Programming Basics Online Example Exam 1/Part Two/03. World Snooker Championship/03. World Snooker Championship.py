dict_camp = {
    'Quarter final':
        {
        'Standard': 55.5, 'Premium': 105.20, 'VIP': 118.90,
        },
    'Semi final': {
        'Standard': 75.88, 'Premium': 125.22, 'VIP': 300.4,
    }, 'Final': {
        'Standard': 110.10, 'Premium': 160.66, 'VIP': 400,
    }
}

price = dict_camp[input()][input()]
ticket = int(input())
shot = input()
price *= ticket

if price > 4000:
    price *= 0.75
    print(f'{price:.2f}')
    exit()

if price > 2500:
    price *= 0.90

if shot == 'Y':
    price += ticket * 40

print(f'{price:.2f}')