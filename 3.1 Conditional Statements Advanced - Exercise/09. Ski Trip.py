days = int(input()) - 1
room = input()
feedback = input()

price = 0
discount  = 0

dict_price = {
    'room for one person': 18.00,
    'apartment': 25.00,
    'president apartment': 35.00
}

if room == 'apartment':
    if days < 10:
        discount = 0.70
    if 10 <= days <= 15:
        discount = 0.65
    if days > 15:
        discount = 0.50
elif room == 'president apartment':
    if days < 10:
        discount = 0.90
    if 10 >= days <= 15:
        discount = 0.85
    if days > 15:
        discount = 0.80

if discount > 0:
    money = dict_price[room] * days * discount
else:
    money = dict_price[room] * days

if feedback == 'positive':
    money *= 1.25
if feedback == 'negative':
    money *= 0.90

print(f'{money:.2f}')


'''
14
apartment
positive

'''