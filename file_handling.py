import os

os.getcwd()

os.chdir("D:\Python Course\Python Projects\File-Handling")

#Write Data
# file=open('file.txt', 'w')
# file.write("I love pakistan\n")
# file.write("I am a python developer\n")
# print("Data Written Successfully!")
# file.close()

#Append

# file=open('file.txt', 'a')
# file.write("Python is the best programming language\n")
# print("Data Written Successfully")
# file.close()

#Read File

# file=open('file.txt', 'r')
# call=file.read()
# print(call)
# file.close()

#Print index

# file=open('file.txt', 'r')
# call = file.read(15)
# print(call)
# file.close()

#Read File Lines by lines..

# file = open('file.txt', 'r')
# call = file.readlines()
# for lines in call:
#     print(lines, end='')
# file.close()


#Create New File

# g=open('file1.txt', 'x')
# g.write("file")
# print("fine")
# g.close()


#Delete File

# os.remove('file1.txt')


#Another condition to delete file


# file = open("file1.txt", 'x')
# file.write("New File")
# print("fine")
# file.close()

# Delete file

if os.path.exists('file1.txt'):
    os.remove('file1.txt')
else:
    print("File does not exist!")

