# Write method in file.

"""file =open("file.txt","w")
file.write("Hello World")
file.close()"""

"""append
file=open("file.txt","a")
file.write("Hello World")
file.close()"""

"""read in console
file=open("file.txt","r")
print(file.read())
file.close()"""

"""
l = []
for i in range(1,11):
    l.append(i)
file=open("file.txt","a")
file.write(str(l))
file.close()
"""
"""
write read
file=open("file2.txt","w+")
file.write("w+ is writing here!!")
print(file.tell()) #tell where cursor is 
file.seek(0) # use to print from when you want 
print(file.read())
file.close()
"""

#r+
file=open("file2.txt","r+")
file.write("r+ is writing here!!")
file.seek(0) #use to print from when you want
print(file.read())
file.close()