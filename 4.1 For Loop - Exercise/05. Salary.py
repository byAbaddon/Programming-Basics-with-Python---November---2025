dict_sites = {"Facebook": 150, "Instagram": 100, "Reddit": 50, }

tabs = [input() for _ in range(int(input()) + 1)]
salary = int(tabs.pop(0))
salary -= sum(dict_sites.get(x,0) for x in tabs)


print(f'You have lost your salary.' if salary <=0 else salary)



'''
3
500
Github.com
Stackoverflow.com
softuni.bg
'''