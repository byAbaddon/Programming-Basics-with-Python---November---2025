t = sum(int(input()) for _ in range(3))  # общо време в секунди

m = t // 60
s = t % 60

print(f'{m}:{s:02d}')



'''
35
45
44

# result: 2:04
'''