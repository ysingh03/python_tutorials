
i = 0
while i <= 40:
    if i < 10:
        i = i+1
        continue
    print(i, end=" ")
    if i >= 35:

        break # stop the loop
    i = i+1

print("####################################")

while True:
    k = int(input("Enter the number \n"))
    if k > 100:
        print("you have entered correct number")
        break
    else:
        print("try again bro")
        continue

