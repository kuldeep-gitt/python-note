'''Python for Beginners #21
for loops'''

#initialization
sum=0

#declare list (iterable object)
a=[1,2,3,4,5]

#for syntax
for num in a:
	#increment sum by num
    sum=sum+num
    print(sum)

#declare tuple (iterable object)
a=(1,2,3,4,5)

for num in a:
	#print every item
    print(num)

#declare dictionary (iterable object)
a={'key1':1,'key2':2,'key3':3}

#declare string (iterable object)
a='String'

for char in a:
	#print every character
	print(char)
