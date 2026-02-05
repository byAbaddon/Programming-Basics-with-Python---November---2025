budget = float(input())
count_product = spend_money = 0

while True:
    product = input()

    if product == 'Stop':
        print(f'You bought {count_product} products for {spend_money:.2f} leva.')
        break

    price_product = float(input())
    count_product += 1

    if count_product % 3 == 0:
        price_product /= 2

    if  spend_money + price_product > budget :
        print(f'You don\'t have enough money!\nYou need {price_product - (budget - spend_money):.2f} leva!')
        break

    spend_money += price_product