# l = 15 # global variable
# def function1(n):
#
#     l = 5  # local variable
#     m = 10 # local variable
#     print(l)
#     print(n, "I am not good")
#
#
# function1("I am good")
# print(l)
# #print(m)
#
# def function2(h):
#
#     global l
#     l = l + 45
#     print(l)
#     print(h)
#
# function2("Hello")

x = 50


def yogi():
    x = 10

    def rashi():
        global x
        x = 100
        print("before calling rashi() x value", x)
        rashi()
        print("after calling rashi() x value", x)


yogi()
print(x)
