budget, statists, wear = [float(input()) for _ in range(3)]

decore =  budget * 0.1
wear *= statists

if statists > 150:
    wear *= 0.9


budget -= wear + decore
if budget >= 0:
    print(f"Action!\nWingard starts filming with {budget:.2f} leva left.")
else:
    print(f'Not enough money!\nWingard needs {abs(budget):.2f} leva more.')



'''
9587.88
222
55.6

'''