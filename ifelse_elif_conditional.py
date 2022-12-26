# var1 = 45
# var2 = 52
#
# print("Provide the value")
# var3 = int(input())
#
# if var3 > var2:
#     print("Greater value")
# elif var3 == 52:
#     print("same")
# else:
#     print("Lesser")


age = int(input("Enter the age in between 7 to 100 only"))
if age < 7 or age > 100:
    print("Please provide correct age")
elif age < 18:
    print("you can not drive")
elif age == 18:
    print("Be present physically")
else:
    print("you can drive")