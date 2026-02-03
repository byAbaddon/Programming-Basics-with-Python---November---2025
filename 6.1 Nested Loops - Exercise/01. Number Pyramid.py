n = int(input())
c = 0
for r in range(1, n + 1):
    row = []
    for _ in range(r):
        c += 1
        row.append(str(c))
        if c == n: break
    print(' '.join(row))
    if c == n: break
