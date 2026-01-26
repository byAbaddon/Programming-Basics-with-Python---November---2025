a, b, o = [input() for _ in range(3)]

if int(b) == 0:
    print(f'Cannot divide {a} by zero')
else:
    r = eval(f'{a} {o} {b}')

    if o in ['+', '-', '*']:
        t = '- odd' if int(r) & 1 else '- even'
        print(a, o, b, '=', r, t)
    else:
        if o == '/':
            r = f'{float(r):.2f}'

        print(a, o, b, '=', r)

'''
10
12
+
'''
