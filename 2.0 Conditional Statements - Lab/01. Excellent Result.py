# print('Excellent!' if float(input()) >= 5.5  else '')


match float(input()) >= 5.5:
    case True:
        print('Excellent!')
