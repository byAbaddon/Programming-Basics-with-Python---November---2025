# d = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
# print(sum(d.get(x,0) for x in input()))

print(sum({'a':1,'e':2,'i':3,'o':4,'u':5}.get(x,0) for x in input()))
