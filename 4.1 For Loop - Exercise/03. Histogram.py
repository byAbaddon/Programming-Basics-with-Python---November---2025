loop = int(input())
p1, p2, p3, p4, p5 = 199, 399, 599, 799, 10000
n1 = n2 = n3 = n4 = n5 = 0

for x in [int(input()) for _ in range(loop)]:
    if x <= p1:
        n1 += 1
    elif x <= p2:
        n2 += 1
    elif x <= p3:
        n3 += 1
    elif x <= p4:
        n4 += 1
    else:
        n5 += 1

for x in [n1, n2, n3, n4, n5]:
    print(f'{x / loop * 100:.2f}%')

