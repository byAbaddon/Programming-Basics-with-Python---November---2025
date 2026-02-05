people = int(input())

lst = [input().lower() for _ in range(people)]

sport = buy = 0

for x in ['back', 'chest', 'legs', 'abs', 'protein shake', 'protein bar']:
    numbers = lst.count(x)
    print(numbers , '-', x)
    if x in ['protein shake', 'protein bar']:
        buy += numbers
    else:
        sport += numbers

print(f'{sport / people * 100:.2f}% - work out')
print(f'{buy / people * 100:.2f}% - protein')



