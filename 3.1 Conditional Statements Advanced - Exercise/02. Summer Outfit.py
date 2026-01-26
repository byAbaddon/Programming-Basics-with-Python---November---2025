degrees, day_time = int(input()), input()

dict_data = {
    'm': {'Morning': 'Sweatshirt and Sneakers', 'Afternoon': 'Shirt and Moccasins', 'Evening': 'Shirt and Moccasins'},
    'a': {'Morning': 'Shirt and Moccasins', 'Afternoon': 'T-Shirt and Sandals', 'Evening': 'Shirt and Moccasins'},
    'e': {'Morning': 'T-Shirt and Sandals', 'Afternoon': 'Swim Suit and Barefoot', 'Evening': 'Shirt and Moccasins'},
}

match degrees:
    case _ if 10 <= degrees <= 18:
        result = dict_data['m'][day_time]
    case _ if 18 < degrees <= 24:
        result = dict_data['a'][day_time]
    case _ if degrees >= 25:
        result = dict_data['e'][day_time]

print(f'It\'s {degrees} degrees, get your {result}.')

'''
16
Morning
'''
