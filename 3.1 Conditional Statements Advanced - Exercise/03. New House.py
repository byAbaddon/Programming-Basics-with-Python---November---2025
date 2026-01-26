flowers, count, budget = input(), int(input()), float(input())
money = 0

flowers_price = {
    'Roses': 5,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3,
    'Gladiolus': 2.50,
}

match flowers:
    case 'Roses' if count > 80:
        money = flowers_price[flowers] * count * 0.90
    case 'Dahlias' if count > 90:
        money = flowers_price[flowers] * count * 0.85
    case 'Tulips' if count > 80:
        money = flowers_price[flowers] * count * 0.85
    case 'Narcissus' if count < 120:
        money = flowers_price[flowers] * count * 1.15
    case 'Gladiolus' if count < 80:
        money = flowers_price[flowers] * count * 1.20
    case _:
        money = flowers_price[flowers] * count

budget -= money

if budget < 0:
    print(f'Not enough money, you need {abs(budget):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {count} {flowers} and {budget:.2f} leva left.')

'''
Roses
55
250
'''
