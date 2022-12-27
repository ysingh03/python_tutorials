f = open("yogi2.txt")

print(f.tell())

print(f.readline())
print(f.tell())
print(f.seek(15))

print(f.readline())
print(f.tell())

f.close()