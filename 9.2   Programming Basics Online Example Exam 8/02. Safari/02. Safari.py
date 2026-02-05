budget = float(input())
lt_fuel = float(input())
dey = input()

fuel = 2.10
gid = 100
total = 0

subtotal = lt_fuel * fuel + gid
if dey == 'Sunday':
    total = subtotal * 0.8
else:
    total = subtotal * 0.9

if budget >= total:
    print(f'Safari time! Money left: {budget - total:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total - budget:.2f} lv.')
