import math

dict_tours = {'W': 2000, 'F': 1200, 'SF': 720}

count_tours = int(input())
points = int(input())
add_points = wins = 0

for _ in range(count_tours):
    t = input()
    wins += 1 if t == 'W' else 0
    add_points += dict_tours[t]

print(f'Final points: {points + add_points}\nAverage points: {math.floor(add_points / count_tours)}\n{wins / count_tours * 100:.2f}%')