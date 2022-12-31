
import math

me = "yogi"

a1 = 3

a = "this is %s %s "%(me, a1)

print(a)

b = "This is {1} {0}"
c = b.format(me, a1)
print(c)

d = f"this is {me} {a1} {math.cos(90)}"
print(d)


