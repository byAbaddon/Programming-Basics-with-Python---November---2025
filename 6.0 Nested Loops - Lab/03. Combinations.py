n = int(input())
count = 0
for a in range(0, n + 1):
    for b in range(0, n + 1):
        for c in range(0, n + 1):
            r = int(a) + int(b) + int(c)
            if r == n:
                count += 1
print(count)
