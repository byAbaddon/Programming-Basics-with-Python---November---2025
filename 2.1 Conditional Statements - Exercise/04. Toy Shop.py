trip, puzzles, dolls, bears, minions, trucks = [float(input()) for _ in range(6)]

total_sum = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2.0
toys_count = puzzles + dolls + bears + minions + trucks

if toys_count >= 50:
    total_sum *= 0.75

total_sum *= 0.9

print(f'Yes! {total_sum  - trip:.2f} lv left.' if total_sum >= trip
      else f'Not enough money! {trip - total_sum:.2f} lv needed.')

'''
40.8
20
25
30
50
10
'''
