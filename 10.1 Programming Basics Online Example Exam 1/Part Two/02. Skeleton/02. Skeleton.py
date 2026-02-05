minutes, sec, long_u_met, sec_m =  int(input()), int(input()), float(input()), int(input())

calc_control = minutes * 60 + sec
calc_time = long_u_met / 120
calc_all_time = calc_time * 2.5
total = (long_u_met  / 100) * sec_m - calc_all_time

if calc_control >= total:
    print(f'Marin Bangiev won an Olympic quota!\nHis time is {total:.3f}.')
else:
    print(f'No, Marin failed! He was {total - calc_control:.3f} second slower.')


