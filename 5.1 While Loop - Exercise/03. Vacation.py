needed_money = float(input())
current_money = float(input())

spend_days = days = 0

while current_money < needed_money:
    action = input()
    amount = float(input())
    days += 1

    if action == 'spend':
        current_money -= amount
        spend_days += 1
        if current_money < 0:
            current_money = 0
    elif action == 'save':
        current_money += amount
        spend_days = 0

    if spend_days == 5:
        print(f'You can\'t save the money.\n{days}')
        break

if current_money >= needed_money:
    print(f'You saved the money for {days} days.')
