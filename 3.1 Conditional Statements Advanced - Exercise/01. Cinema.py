types, rows, cols = input(), float(input()), float(input())
dict_projections = {'Premiere': 12.00, 'Normal': 7.50, 'Discount': 5.00}

print(f'{dict_projections[types] * (rows * cols):.2f}', 'leva')


'''
Premiere
10
12
'''