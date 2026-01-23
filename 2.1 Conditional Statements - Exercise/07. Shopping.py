budget = float(input())
cards, cpu, ram = [int(input()) for _ in range(3)]

m_cards = cards * 250
m_cpu = cpu *  (m_cards * 0.35)
m_ram = ram * (m_cards * 0.10)

subtotal = m_cards + m_cpu + m_ram
if cards > cpu:
    subtotal *= 0.85

budget -= subtotal
if budget >= 0:
    print(f'You have {budget:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget):.2f} leva more!')



'''
900
2
1
3


920.45
3
1
1
'''