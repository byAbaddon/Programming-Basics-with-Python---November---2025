name = input()
points = float(input())
finish_points = 1250.5

for _ in range(int(input())):
    act = input()
    point = float(input())

    points += len(act) * point / 2
    if points > finish_points:
        print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
        break

if points < finish_points:
    print(f'Sorry, {name} you need {finish_points - points:.1f} more!')

'''
Zahari Baharov
205
4
Johnny Depp
45
Will Smith
29
Jet Lee
10
Matthew Mcconaughey
39
'''
