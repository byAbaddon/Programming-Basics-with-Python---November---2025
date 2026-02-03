p_n = n_n = 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for n in [x for x in iter(input, 'stop')]:
    if int(n) < 0:
        print('Number is negative.')
        continue
    if is_prime(int(n)):
        p_n += int(n)
    else:
        n_n += int(n)

print(f'Sum of all prime numbers is: {p_n}')
print(f'Sum of all non prime numbers is: {n_n}')
