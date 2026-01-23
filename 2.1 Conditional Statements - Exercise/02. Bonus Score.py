n = int(input())
bonus = 0

if n <= 100:
    bonus = 5
elif n <= 1000:
    bonus = n * 0.2
else:
    bonus = n * 0.1

if not n & 1:
    bonus += 1
elif n % 5 == 0:
    bonus += 2

print(f'{bonus}\n{n + bonus}')
