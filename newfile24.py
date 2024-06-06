# The function that enables us to work with files in python is the open function
# The open function accepts the name of the file as a string argument and returns a file object
# Also the open function accepts a second argument that specifiex the mode in which the file is to be opened
# f = open("exercises.py")
# print(f)

# The four different kind of modes to open a file
# 1 Read mode: r
# 2 Append mode: a
# 3 Write mode: w
# 4 Create mode: x
# 5 binary mode: b
# 6 text mode: t
# Read mode is the default mode to open a file
# The read function enables us to read the contents of a file opened in read mode


# f=open("nine24.py","r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# 
# print(f.read(15))

# for x in f :
#     print(x)
# f.close()    


# f=open("filesystem24.txt" ,"r")
# print(f.read())
# for y in f:
#     print(y)

# print(f.readline())

# g= open ("filesystem24.txt","a")
# print(g.write("name of my school"))
# g.close()
# g=open("filesystem24.txt","r")
# print(g.read())


# print(g.write("name of my school"))

f= open("Add2.py","x")
print(f.write("Good morning"))