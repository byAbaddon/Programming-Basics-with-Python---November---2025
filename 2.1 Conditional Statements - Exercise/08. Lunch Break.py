from math import ceil

movie, time, time_rest = input(), int(input()), int(input())

t_lunch = time_rest * 0.125
t_rest = time_rest * 0.25
total_time = time_rest - (t_lunch + t_rest)

if total_time >= time:
    print(f'You have enough time to watch {movie} and left with {ceil(total_time - time)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {movie}, you need {ceil(time - total_time)} more minutes.')

'''
Teen Wolf
48
60

'''
