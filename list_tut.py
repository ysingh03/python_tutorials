## List is mutable or can change the values

list_data = [10, 20, 30, 300, 25.7, 'chips', True, 40, 120, 600, 90]

print(list_data[0])
print(len(list_data))
print(list_data[6])
print(list_data[0:4])
print(list_data[0:6:2])
print(list_data[:])

#list_data.sort()
print(list_data)
#list_data.reverse()
print(list_data)
list_data.append(23)
print(list_data)
list_data.remove(23)
print(list_data)
# #list_data.min()
# print(list_data)
# #list_data.max()
# print(list_data)
list_data.insert(3, 125)
print(list_data)
list_data.pop()
print(list_data)
list_data[4] = 135
print(list_data)