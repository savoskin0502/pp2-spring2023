f = open('rawdata.txt', mode='r')
# s = f.read()
# print(s, type(s))

# s = f.readline()
# print(s, type(s))
# print(f.readline())

s = f.readlines()
print(s, type(s))

f.close()
