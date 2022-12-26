# Dictionary is nothing but key value pairs

#dictionary blank
d1 = {}
print(type(d1))

d2 = {'one': 1, 2: 'two', 'three': 'three', 4: [1, 3, 5, 6], 5: (12, 10, 113)}
print(d2)
print(d2["three"])
print(d2[4])
d2[25] = 'Hello'
print(d2)
del d2[25]
print(d2)
d3 = d2.copy()
print(d3)
print(d3.get(2))
d3.update({'name': 'yogi'})
print(d3)
print(d2)
print(d3.keys())
print(d3.values())
print(d3.items())

data = input("Please see the values of provided key")
print(d3[data])
