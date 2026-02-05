lst = [x for x in iter(input, 'End of tournaments')]

name = ''
w_points = l_points = count = 0
w_games = l_games = 0

while len(lst):
    name = lst.pop(0)

    mach = int(lst.pop(0))
    count += mach
    for i in range(1, mach + 1):
        w_points = int(lst.pop(0))
        l_points = int(lst.pop(0))
        status = 'win'
        if w_points > l_points:
            w_games += 1
        else:
            l_games += 1
            status = 'lost'

        print(f'Game {i} of tournament {name}: {status} with {abs(w_points - l_points)} points.')

print(f'{w_games / count * 100:.2f}% matches win')
print(f'{l_games / count * 100:.2f}% matches lost')
