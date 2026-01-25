lst_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', ]

day = input()

print('Error' if not day in lst_days else 'Weekend' if day == 'Saturday' or day == 'Sunday' else 'Working day')
