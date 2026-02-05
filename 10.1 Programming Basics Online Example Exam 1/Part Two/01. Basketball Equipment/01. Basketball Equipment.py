year_price = int(input())

price_sneakers = year_price * 0.6
price_equip = price_sneakers * 0.8
price_ball = price_equip * 0.25
price_accessories = price_ball * 0.20

total = year_price + price_sneakers + price_equip + price_ball + price_accessories
print(f'{total:.2f}')
