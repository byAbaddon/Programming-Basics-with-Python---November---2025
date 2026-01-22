prices = [5.8, 7.2, 1.2]
subtotal = sum(int(input()) * prices[i] for i in range(3))
discount = int(input())
print(subtotal * (1 - discount / 100))

'''
2
3
4
25
'''
