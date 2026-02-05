years, type_contract, add_net, mounts = input(), input(), input(), int(input())

dict_contracts = {
    'one': {
        'Small': 9.98, 'Middle': 18.99, 'Large': 25.98, 'ExtraLarge': 35.99
    },
    'two': {
        'Small': 8.58, 'Middle': 17.09, 'Large': 23.59, 'ExtraLarge': 31.79
    }
}

price = dict_contracts[years][type_contract]

if add_net == 'yes':
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

if years == 'two':
    price *= 0.9625

print(f'{price * mounts:.2f} lv.')
