from math import prod

aquarium = prod(int(input()) for _ in range(3)) / 1000
percent = float(input()) / 100
print(aquarium * (1- percent))

'''
105
77
89
18.5

#586.445475
'''
