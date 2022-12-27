# Health Management System

# Health Management System
# 3 clients - Harry, Rohan and Hammad
def getdate():
    import datetime
    return datetime.datetime.now()


task = input('WAHT DO YOU WANT TO DO READ OR ADD: ')
if task == 'Add' or task == "add" or task == "ADD":
    patient = input('WRITE \n 1 for Harry\n 2 for Rohan \n3 for Hammad \n')
    if patient == "1":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("harry1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("harry2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    elif patient == "2":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("rohan1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("rohan2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    elif patient == "3":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("hammed1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("hammed2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    else:
        print("you pressed wrong key")
elif task == 'read' or task == 'READ' or task == 'Read':
    thing = input("Press 1 for exercise 2 for food")

    if thing == "1":
        person = input("PRESS 1 FOR HARRY 2 FOR ROHAN AND 3 FOR HAMMMED")
        if person == '1':

            q = open("harry1.txt")
            text = q.read()
            print(text)
        elif person == '1':
            q = open("rohan1.txt")
            text = q.read()
            print(text)
        elif person == '3':
            q = open("hammed1.txt")
            text = q.read()
            print(text)

    elif thing == "2":
        person = input("PRESS 1 FOR HARRY 2 FOR ROHAN AND 3 FOR HAMMMED")
        if person == '1':

            q = open("harry2.txt")
            text = q.read()
            print(text)
        elif person == '1':
            q = open("rohan2.txt")
            text = q.read()
            print(text)
        elif person == '3':
            q = open("hammed2.txt")
            text = q.read()
            print(text)

print("THANK YOU FOR USING KAVYA MITTAL SERVICES")