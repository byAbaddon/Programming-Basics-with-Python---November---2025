money = 0

while True:
    token = input()
    if len(token) < 10:
        if float(token) > 0:
            print(f'Increase: {float(token):.2f}')
            money += float(token)
        else:
            print('Invalid operation!')
            break
    else:
        break

print(f'Total: {float(money):.2f}')