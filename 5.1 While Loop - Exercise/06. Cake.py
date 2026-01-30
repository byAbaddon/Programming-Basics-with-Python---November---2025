cake = int(input()) * int(input())

while True:
    token = input()
    if token == "STOP":
        print(cake, 'pieces are left.')
        break
    if cake <= int(token):
        print(f'No more cake left! You need {int(token) - cake} pieces more.')
        break
    cake -= int(token)
