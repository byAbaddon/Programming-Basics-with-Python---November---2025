n = int(input())

for x in range(1111, 10000):
    is_special = True

    for d in str(x):
        d = int(d)

        if d == 0 or n % d != 0:
            is_special = False
            break

    if is_special:
        print(x, end=' ')
