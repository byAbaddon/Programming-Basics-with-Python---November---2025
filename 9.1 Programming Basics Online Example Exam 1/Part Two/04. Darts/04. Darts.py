name = input()

points = 301
good_shots = 0
wrong_shots = 0

while True:
    token = input()
    if token == 'Retire':
        print(f'{name} retired after {wrong_shots} unsuccessful shots.')
        break

    shot = int(input())

    if token == 'Single':
        if points - shot >= 0:
            points -= shot
            good_shots += 1
        else:
            wrong_shots += 1
    elif token == 'Double':
        if points - shot * 2 >= 0:
            points -= shot * 2
            good_shots += 1
        else:
            wrong_shots += 1
    else:
        if points - shot * 3 >= 0:
            points -= shot * 3
            good_shots += 1
        else:
            wrong_shots += 1

    if points == 0:
        print(f'{name} won the leg with {good_shots} shots.')
        break
