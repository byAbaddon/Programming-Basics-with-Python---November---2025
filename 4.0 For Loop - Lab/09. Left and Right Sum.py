l = [int(input()) for _ in range(int(input()) * 2)]

a = sum(l[0:len(l) // 2])
b = sum(l[len(l) // 2:])

print(f'Yes, sum = {a}' if a == b else f'No, diff = {abs(b - a)}')
