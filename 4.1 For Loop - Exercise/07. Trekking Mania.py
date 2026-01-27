groups = [int(input()) for _ in range(int(input()))]
all_people = sum(groups)

def calc(min_val, max_val):
    current_group = sum(filter(lambda x: min_val <= x <= max_val, groups))
    return f'{current_group / all_people * 100:.2f}%'


print(calc(0, 5), calc(6, 12), calc(13, 25), calc(26, 40), calc(41, 1000),sep='\n')

