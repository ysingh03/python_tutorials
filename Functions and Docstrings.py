
a = 10
b = 300

c = sum((a, b)) # built in functions
print(c)

# User created functions

def function1():
    print("Hello All ")

function1()

def function2(x, y):
    """This is a function which will calculate average of two numbers"""
    result = (x+y)/2
    return result

z = function2(23, 45)
print(z)

print(function2.__doc__)
