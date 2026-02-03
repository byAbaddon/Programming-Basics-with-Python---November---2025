destination = input()

while destination != 'End':
    budget = float(input())
    money = 0

    while budget > money:
        tips = float(input())
        money += tips

    print(f'Going to {destination}!')
    destination = input()
