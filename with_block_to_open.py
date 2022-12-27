# with open("yogi2.txt", "rt") as f:
#     a = f.readlines()
#     print(a)
#
# b = open("yogi2.txt")
# print(b.read())


with open("yogi2.txt") as f:
    a = f.read(8)
    print(a)
f = open("yogi.txt", "rt")
print(f.read())

f.close()