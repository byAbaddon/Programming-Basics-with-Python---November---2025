jury = int(input())
grade = 0
lst = []

while True:
    pre = input()
    if pre == 'Finish':
        break

    for i in range(jury):
        grade += float(input())

    print(f'{pre} - {grade / jury:.2f}.')
    lst += [grade / jury]
    grade = 0

print(f'Student\'s final assessment is {sum(lst) / len(lst):.2f}.')
