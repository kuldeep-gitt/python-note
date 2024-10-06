#Access modes
#r
#w
#r+
#w+
#a
#a+

#read a file
file = open('D:\\test.txt',mode='r')
print(file.read())
file.seek(0)
print(file.readlines())
file.close()

#write to a file
file = open('D:\\test.txt',mode='w')
file.write('Hello World\nBitten Tech\nTechHacker')
file.close()

#read a file
file = open('D:\\test.txt',mode='r')
print(file.read())
file.close()

#append to a file
with open('D:\\test.txt',mode='a') as file:
    file.write('Hello World\nBitten Tech\nTechHacker')

file = open('D:\\test.txt',mode='r')
print(file.read())



