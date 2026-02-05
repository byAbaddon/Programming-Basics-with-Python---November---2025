strawberries = float(input())
banans_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2
strawberries_price = strawberries

total = strawberries_price * strawberries_kg + raspberries_price * raspberries_kg + oranges_price * oranges_kg + bananas_price * banans_kg
print(f'{total:.2f}')
