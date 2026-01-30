from math import floor

money = float(input())
counter = 0
coins = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

for i in range(len(coins)):
    counter += floor(money / coins[i])
    money = round(money % coins[i], 2)
print(counter)

#2.73 //5
#0.03 //2