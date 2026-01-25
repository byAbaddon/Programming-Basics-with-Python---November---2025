city = input()
money = float(input())
result = 0

info_dict = {
    'Sofia': {'s': 5, 'm': 7, 'l': 8, 'xl': 12},
    'Varna': {'s': 4.5, 'm': 7.5, 'l': 10, 'xl': 13},
    'Plovdiv': {'s': 5.5, 'm': 8, 'l': 12, 'xl': 14.5}
}

if not (city in info_dict) or money < 0:
    print("error")
    exit()

if money <= 500:
    result = (info_dict[city]['s'] * money) / 100
elif 500 < money <= 1000:
    result = (info_dict[city]['m'] * money) / 100
elif 1000 < money <= 10000:
    result = (info_dict[city]['l'] * money) / 100
elif money > 10000:
    result = (info_dict[city]['xl'] * money) / 100

print(f'{result:.2f}')

# Varna
# 3874.50