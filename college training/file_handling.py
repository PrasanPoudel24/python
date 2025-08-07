#file handling -> create,update,delete, read
#mode = r,w,a, r+ ,w+ ,a+
#delete ->os -> modules import ->delete

# r -> read  -> file should be present
"""
fs = open("hello.txt",mode="r")

#read properties -> read(), readline() , readlines()
#print(fs.read())
print(fs.readline())
#print(fs.readlines())

#close the file
fs.close()


#write

fs1=open("hello.txt",mode="w")
fs1.write("hello world")
fs1.close()


#write+ -> read and write
fs1=open("hello.txt",mode="w+")
fs1.write("hello world feri")
fs1.seek(0)#zero index ma bascha
one=fs1.read()
print(one)
fs1.close()

#append mode

fs1=open("hello.txt",mode="a+")
fs1.write("hello prasan")
fs1.seek(0)#zero index ma bascha
one=fs1.read()
print(one)
fs1.close()


"""


#delete
import os
os.remove("hello1.txt")