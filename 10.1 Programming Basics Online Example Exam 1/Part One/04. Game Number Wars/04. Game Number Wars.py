f_player_name, s_player_name = input(), input()
f_points = s_points = 0

while True:
    try:
        f_card = int(input())
        s_card = int(input())
        if f_card > s_card:
            f_points += f_card - s_card
        elif s_card > f_card:
            s_points += s_card - f_card
        else:
            print(f'Number wars!')
            f_card = int(input())
            s_card = int(input())
            if f_card > s_card:
                print(f'{f_player_name} is winner with {f_points} points')
            else:
                print(f'{s_player_name} is winner with {s_points} points')
            break
    except:
        print(f'{f_player_name} has {f_points} points')
        print(f'{s_player_name} has {s_points} points')
        break

