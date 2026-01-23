n = int(input())

match n:
    case _ if n < 100:
        print('Less than 100')
    case _ if 100 <= n <= 200:
        print('Between 100 and 200')
    case _:
        print('Greater than 200')

