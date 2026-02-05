w = l = d = 0

for m in [input() for _ in range(3)]:
    f,s = m.split(':')
    if f > s: w+= 1
    elif f < s: l+= 1
    else: d+= 1


print(f'Team won {w} games.\nTeam lost {l} games.\nDrawn games: {d}')

'''
3:1
0:2
0:0
'''
