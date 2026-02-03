s, e, n = [int(input()) for _ in range(3)]

count = 0
for a in range(s, e + 1):
    for b in range(s, e + 1):
        r = a + b
        count += 1
        if r == n:
            print(f'Combination N:{count} ({a} + {b} = {r})')
            exit()

print(f'{count} combinations - neither equals {n}')
