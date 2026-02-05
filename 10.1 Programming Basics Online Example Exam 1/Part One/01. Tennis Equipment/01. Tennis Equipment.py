from math import floor, ceil

price_rocket = float(input())
count_rocket = int(input())
count_sneakers = int(input())

rocket = count_rocket * price_rocket
sneakers = count_sneakers * price_rocket / 6
subtotal = (rocket + sneakers) * 0.2
total = rocket + sneakers + subtotal

print(f'Price to be paid by Djokovic {floor(total / 8)}')
print(f'Price to be paid by sponsors {ceil(total * 7 / 8)}')

'''
850
4
2
'''
