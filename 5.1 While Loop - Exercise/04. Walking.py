steps = 10000
count_steps = 0

while True:
    token = input()
    if len(token) > 8:
        count_steps += int(input())
        break

    count_steps += int(token)
    if count_steps >= steps: break

if count_steps >= steps:
    print(f'Goal reached! Good job!\n{count_steps - steps} steps over the goal!')
else:
    print(f'{abs(steps - count_steps)} more steps to reach goal.')