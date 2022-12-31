# Health Management System

# Health Management System
# 3 clients - Harry, Rohan and Hammad
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# task = input('WAHT DO YOU WANT TO DO READ OR ADD: ')
# if task == 'Add' or task == "add" or task == "ADD":
#     patient = input('WRITE \n 1 for Harry\n 2 for Rohan \n3 for Hammad \n')
#     if patient == "1":
#         k = input("Write \n 1 for Exercise and 2 for Food ")
#         if k == "1":
#             h = open("harry1.txt", "a")
#             exercise = input("WRITE YOUR EXERCISE ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {exercise}\n")
#         elif k == "2":
#             h = open("harry2.txt", "a")
#             Food = input("WRITE YOUR FOOD ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {Food}\n")
#     elif patient == "2":
#         k = input("Write \n 1 for Exercise and 2 for Food ")
#         if k == "1":
#             h = open("rohan1.txt", "a")
#             exercise = input("WRITE YOUR EXERCISE ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {exercise}\n")
#         elif k == "2":
#             h = open("rohan2.txt", "a")
#             Food = input("WRITE YOUR FOOD ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {Food}\n")
#     elif patient == "3":
#         k = input("Write \n 1 for Exercise and 2 for Food ")
#         if k == "1":
#             h = open("hammed1.txt", "a")
#             exercise = input("WRITE YOUR EXERCISE ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {exercise}\n")
#         elif k == "2":
#             h = open("hammed2.txt", "a")
#             Food = input("WRITE YOUR FOOD ")
#             h.write(f"[{str(getdate())}]")
#             h.write(f" {Food}\n")
#     else:
#         print("you pressed wrong key")
# elif task == 'read' or task == 'READ' or task == 'Read':
#     thing = input("Press 1 for exercise 2 for food")
#
#     if thing == "1":
#         person = input("PRESS 1 FOR HARRY 2 FOR ROHAN AND 3 FOR HAMMMED")
#         if person == '1':
#
# #             q = open("harry1.txt")
# #             text = q.read()
# #             print(text)
# #         elif person == '1':
# #             q = open("rohan1.txt")
# #             text = q.read()
# #             print(text)
# #         elif person == '3':
# #             q = open("hammed1.txt")
# #             text = q.read()
# #             print(text)
# #
# #     elif thing == "2":
# #         person = input("PRESS 1 FOR HARRY 2 FOR ROHAN AND 3 FOR HAMMMED")
# #         if person == '1':
# #
# #             q = open("harry2.txt")
# #             text = q.read()
# #             print(text)
# #         elif person == '1':
# #             q = open("rohan2.txt")
# #             text = q.read()
# #             print(text)
# #         elif person == '3':
# #             q = open("hammed2.txt")
# #             text = q.read()
# #             print(text)
# #
# # print("THANK YOU FOR USING KAVYA MITTAL SERVICES")
#
# ####################################################################
#
# def gettime():
#     import datetime
#     return datetime.datetime.now()
#
#
# def log():
#     print("Choose your client")
#     client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
#     con = 1
#     if client == 1:
#         while con == 1:
#             print("What do you want to log for Harry?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("harry diet.txt", "a")
#                 data = input("Enter what has Harry Eaten?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#
#             else:
#                 f = open("harry exercise.txt", "a")
#                 data = input("How much time has Harry worked out?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#             con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
#
#     elif client == 2:
#         while con == 1:
#             print("What do you want to log for Rohan?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("rohan diet.txt", "a")
#                 data = input("Enter what has Rohan Eaten?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#
#             else:
#                 f = open("rohan exercise.txt", "a")
#                 data = input("How much time has Rohan worked out?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#             con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))
#
#     elif client == 3:
#         while con == 1:
#             print("What do you want to log for Hammad?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("hammad diet.txt", "a")
#                 data = input("Enter what has Hammad Eaten?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#
#             else:
#                 f = open("hammad exercise.txt", "a")
#                 data = input("How much time has Hammad worked out?")
#                 f.write(str([str(gettime())]) + "  " + data + "\n")
#                 f.close()
#             con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))
#
#
# def retrieve():
#     con = 1
#     while con == 1:
#         print("Choose your client")
#         client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
#         if client == 1:
#             print("What do you want to retrieve for Harry?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("harry diet.txt", "r")
#                 print(f.readlines())
#                 f.close()
#
#             else:
#                 f = open("harry exercise.txt", "r")
#                 print(f.readlines())
#                 f.close()
#
#         elif client == 2:
#             print("What do you want to retrieve for Rohan?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("rohan diet.txt", "r")
#                 print(f.readlines())
#                 f.close()
#
#             else:
#                 f = open("rohan exercise.txt", "r")
#                 print(f.readlines())
#                 f.close()
#
#         elif client == 3:
#             print("What do you want to retrieve for Hammad?")
#             choice = int(input("1. Diet \n2. Activity"))
#             if choice == 1:
#                 f = open("hammad diet.txt", "r")
#                 print(f.readlines())
#                 f.close()
#
#             else:
#                 f = open("hammad exercise.txt", "r")
#                 print(f.readlines())
#                 f.close()
#     con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No"))
#
#
# print("Welcome to Health care Management System")
# ch = int(input("What do you want to do? \n1. Log \n2. Retrieve"))
# if ch == 1:
#     log()
# elif ch == 2:
#     retrieve()
# else:
#     print("Wrong Input. Please try again.")
#
#
########################################################################################

# Health Management System

client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}

lock_list = {1: "Exercise", 2: "Diet"}





def getdate():

    import datetime

    return datetime.datetime.now()





try:

    print("Select Client Name:")

    for key, value in client_list.items():

        print("Press", key, "for", value, "\n", end="")

    client_name = int(input())



    print("Selected Client : ", client_list[client_name], "\n", end="")



    print("Press 1 for Lock")

    print("Press 2 for Retrieve")

    op = int(input())



    if op is 1:

        for key, value in lock_list.items():

            print("Press", key, "to lock", value, "\n", end="")

        lock_name = int(input())

        print("Selected Job : ", lock_list[lock_name])

        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")

        k = 'y'

        while (k is not "n"):

            print("Enter", lock_list[lock_name], "\n", end="")

            mytext = input()

            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")

            k = input("ADD MORE ? y/n:")

            continue

        f.close()

    elif op is 2:

        for key, value in lock_list.items():

            print("Press", key, "to retrieve", value, "\n", end="")

        lock_name = int(input())

        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")

        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")

        contents = f.readlines()

        for line in contents:

            print(line, end="")

        f.close()

    else:

        print("Invalid Input !!!")

except Exception as e:

    print("Wrong Input !!!")