#range
for i in range(100,50,-2):
    #print(i)
    pass
result=list(range(0,10))
print(result)

#enumerate
string = 'subscribe'
count=0
for j,i in enumerate(string):
    print (j,i)

#zip
list1 = [1,2,3,4,5,11,12,13]
list2 = [6,7,8,9,10]

for j,i in zip(list1, list2):
    print(j,i)

#in
print(10 in {'key':10})

#max, min
list1=list(range(10))
print(min(list1))
print(max(list1))

#random, shuffle, randint
from random import random
list1=[1,2,3,4,5]
num = random()
num = randint(0,100)
shuffle(list1)
print(num)

#type function
a = (1,2,3)
print(type(a))