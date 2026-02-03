s, e = int(input()), int(input())
counter = odd = even = 0
lst = []
for x in range(s, e + 1):
    for i in str(x):
        counter += 1
        if counter & 1:
            odd += int(i)
        else:
            even += int(i)

    if odd == even:
        lst.append(x)
    counter = odd = even = 0

print(*lst)