import math

record, distance, sec = [float(input()) for _ in range(3)]

slowdowns = math.floor(distance / 15) * 12.5
total_time = distance * sec + slowdowns

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record:.2f} seconds slower.')


'''
10464
1500
20

#-------------
55555.67
3017
5.03

 Yes, he succeeded! The new world record is 17688.01 seconds.
'''
