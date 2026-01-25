match input():
    case 'dog':
        kind = 'mammal'
    case 'crocodile' | 'tortoise' | 'snake':
        kind = 'reptile'
    case _:
        kind = 'unknown'

print(kind)
