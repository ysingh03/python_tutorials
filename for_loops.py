list1 = ["yogi", "gogi", "mitu", "ganu"]

for i in list1:
    print("The name is", i)

print("*************************")

list2 = [["yogi", 35], ["rashi", 30], ["mitu", 8], ["ganu", 4]]

for j, k in list2:
    print(j, "age is", k)

print("*************************")

dict1 = dict(list2)
print(dict1)
print("*************************")
for j, k in dict1.items():
    print(j, "age is", k)

print("*************************")
# to print only key of the dict we do below
for item in dict1:
    print(item)

print("*************************")
# to print only key of the dict we do below
for item in dict1.keys():
    print(item)

print("*************************")
# to print only key of the dict we do below
for value in dict1.values():
    print(value)


print("##############################")
list3 = ["yogesh", 1, 10, 3, 7, True, 8.5, 100, 70, 6]

for i in list3:
    if str(i).isnumeric() and i >= 6:
        print(i)
