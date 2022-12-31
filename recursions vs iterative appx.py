# def factorial_iterative(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i + 1)
#     return fact
#
#
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#
#     else:
#         return n * factorial_iterative(n - 1)
#
#
# number = int(input("Enter the number"))
# print("Factorial using iterative method", factorial_iterative(number))
# print("Factorial using recursive method", factorial_recursive(number))

# 0,1,1,2,3,5,8,13,21
def fabo_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabo_function(n-1)+fabo_function(n-2)


number = int(input("Enter the number"))
print(fabo_function(number))


