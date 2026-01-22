obj_price = {'chicken' : 10.35 , 'fish' : 12.40 , 'vegetable': 8.15, 'delivery': 2.50, 'discount': 20}
keys= list(obj_price.keys())[0:3]
purchase = sum(int(input()) * obj_price[v]  for v in keys)
dessert = purchase * obj_price['discount'] / 100
print(purchase + dessert + obj_price['delivery'])

'''
2
4
3
'''