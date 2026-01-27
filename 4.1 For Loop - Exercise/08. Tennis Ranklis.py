from math import floor

n, start = int(input()), int(input())
p = {'W':2000,'F':1200,'SF':720}
r = [input() for _ in range(n)]

print(f'Final points: {start + sum(p[x] for x in r)}')
print(f'Average points: {floor(sum(p[x] for x in r)/n)}')
print(f'{r.count("W")/n*100:.2f}%')



'''
5
1400
F
SF
W
W
SF

'''