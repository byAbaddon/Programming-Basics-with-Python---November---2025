bad_limit = int(input())
bad_left = bad_limit
total = count = 0
last = ''

while True:
    token = input()
    if token == 'Enough':
        print(f'Average score: {total / count:.2f}\nNumber of problems: {count}\nLast problem: {last}')
        break

    grade = int(input())
    total += grade
    count += 1
    last = token

    if grade <= 4:
        bad_left -= 1
        if bad_left == 0:
            print(f'You need a break, {bad_limit} poor grades.')
            break
