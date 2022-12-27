# file to basics

"""
"r" - Open the file for reading
"w" - open the file for writing
"x" - create file if not exists
"a" - add more content in the file
"t" - text mode
"b" - binary mode
"+" - read and write
"""

# file writing

f = open("yogi.txt")
content = f.read(5)
print(content)

f = open("yogi.txt", "r")
content = f.read()
print(content)

f = open("yogi.txt", "rt")
print(f.readline())
content = f.read()

f = open("yogi.txt", "r")
content = f.readlines()


h = open("yogi3.txt", "w")
b = h.write("Hello All, I am good boy\n")

g = open("yogi2.txt", "a")
a = g.write("Hello All, I am good boy\n")


# Handle to read and write both

j = open("yogi3.txt", "r+")
print(j.read())
j.write("Thanks you\n")



f.close()

