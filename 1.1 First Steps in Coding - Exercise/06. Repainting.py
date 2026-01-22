nylon, paint, diluent, hours = [int(input()) for _ in range(4)]

nylon = (nylon + 2) * 1.5
paint = (paint * 1.1) * 14.5
diluent = diluent * 5.0

total_materials = nylon + paint + diluent + 0.4
masers_price = total_materials * 0.30 * hours

print(total_materials + masers_price)

'''
10
11
4
8

output: 727.09 
'''