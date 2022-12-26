
num1 = input("Enter the number \n")
num2 = input("Enter the number \n")

try:
    print("The sum of these number is ", int(num1)+int(num2))

except Exception as e:
    print(e)

print("This line always show")

