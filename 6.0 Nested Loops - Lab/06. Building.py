fl, app = int(input()), int(input())

first = fl
collect = ''

for e in range(fl, 0, -1):
    for r in range(app):
        if e == first:
            collect += f"L{e}{r} "
        elif e & 1:
            collect += f"A{e}{r} "
        else:
            collect += f"O{e}{r} "

    print(*(collect.split(' ')))
    collect = ''
