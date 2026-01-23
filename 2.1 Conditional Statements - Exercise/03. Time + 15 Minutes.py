h = int(input())
m = int(input()) + 15

if m >= 60:
    h += m // 60
    m = m % 60
if h == 24:
    h = 0

print(f'{h}:{m:02d}')

'''
1
46
'''
