s, w, h = int(input()), int(input()), int(input())
room = s * w * h
kb = 0

while True:
    token = input()
    if token == 'Done':
        print(f'{room - kb} Cubic meters left.')
        break
    kb += int(token)
    if kb > room:
        print(f'No more free space! You need {kb - room} Cubic meters more.')
        break
