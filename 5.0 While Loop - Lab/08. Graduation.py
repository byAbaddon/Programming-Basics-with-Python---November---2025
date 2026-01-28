name = input()
grade, cls, fall = 0, 0, 0

while cls < 12:
    token = float(input())

    if token >= 4:
        cls += 1
        grade += token
    else:
        fall += 1

    if fall == 2: break

if fall == 2:
    print(f'{name} has been excluded at {cls + 1} grade')
else:
    print(f'{name} graduated. Average grade: {grade / cls:.2f}')
