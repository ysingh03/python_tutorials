# n = int(input("Enter the no of rows: "))
# l = int(input("Enter either 0 or 1: "))
# if bool(l) == True:
#     for x in range(n):
#         for y in range(x + 1):
#             print("*", end=" ")
#         print("\n")
# else:
#     for x in range(n):
#         for y in range(n - x):
#             print("*", end=" ")
#         print("\n")
#
# print("How many lines you want to print")
# num = int(input())
# tpe = int(input("Enter your type 1/0:\n"))
# for t in range(1, num + 1):
#     if tpe == 1:
#         print("*" * t, end=" \n")
# for b in range(num + 1, 0, -1):
#     if tpe == 0:
#         print("*" * b, end=" \n")
#
# ##########################################################################
#
# a = int(input("enter the number of rows you want to print"))
# b = bool(int(input("choose 0 or 1")))
# c = 1
# while True:
#     if b == True and c <= a:
#         print(c * "*")
#         c = c + 1
#     elif c > a:
#         break
#     if b == False and a > 0:
#         print(a * "*")
#         a = a - 1
#     elif a == 0:
#         break
#
# ##########################################################################
#
# a = int(input("enter the number of rows you want to print: \n"))
# b = input('enter 0 or 1:\n ')
# if b == "1":
#     for i in range(1, a + 1, 1):
#         print("*" * i)
# elif b == "0":
#     for i in range(a, 0, -1):
#         print("*" * i)
# else:
#     print('please enter correct boolean')
#
# ##########################################################################
#
# n = int(input('Enter how many row you want to print: '))
# boolean = int(input('type 1 or 0: '))
#
# if boolean == 1:
#     for i in range(n + 1):
#         print('*' * i)
# elif boolean == 0:
#     for i in range(n + 1):
#         print('*' * (n - i))
# else:
#     print('You have to enter 1 or 0.')
#
# ##########################################################################
#
# print('Solution for Exercise 4!')
#
# print("Enter the number of rows you want in your pattern.")
# v = int(input())
#
# bool_value = int(input("Enter the value as 0 or 1. To Decide what will be the direction of your pattern."))
#
# if bool_value == 1:
#     bool_value = True
#     i = 0
#     while i < v:
#         print("*" * i)
#         i += 1
#
# elif bool_value == 0:
#     bool_value = False
#     t = v
#     while t > 0:
#         print("*" * t)
#         t -= 1
# else:
#     print("This number is not valid.")
#
# ##########################################################################
#
# n = int(input("Number of rows : "))
# x = int(input("Give 1 for pyramid, 0 for reverse pyramid : "))
# flag = True
# if x == 0:
#     flag = False
#
# if flag:
#     for star in range(1, n+1):
#         print(star * "*")
# else:
#     for star in range(n, 0, -1):
#         print(star * "*")
#

############### with if and for #############################################
#
# print("Pattern printing")
# num = int(input("Enter how many rows you want : "))
# print("enter 1 or 0")
# bool_value = int(int(input("1 for True and 0 for False : ")))
# if bool_value == 1:
#     for i in range(0, num+1):
#         print("*" * i)
#
# if bool_value == 0:
#     for i in range(num, 0, -1):
#         print("*" * i)

################## with try and while #######################################

try:
    n = int(input("Enter the row : "))
    b = int(input("Enter the pattern(0 to 1) : "))
    if b is 1:
        count = 0
        while count <= n:
            print("#" * count, end="")
            print("\n", end="")
            count = count + 1

    elif b is 0:
        count = n
        while count != 0:
            print("#" * count, end="")
            print("\n", end="")
            count = count + 1

    else:
        print("Invalid Pattern !!!")
except Exception as e:
    print("Invalid Input !!!")





