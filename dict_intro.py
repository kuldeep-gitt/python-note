'''Python for Beginners #15
Introduction to Dictionaries'''

#Declaration
dict={"key1":"value1","key2":"value2","key3":"value3"}

print("Dictionary keys:",dict.keys())

print("Dictionary Values:",dict.values())

print("Dictionary Items:",dict.items())

print("Value of key1:",dict['key1'])

#Updation
dict['key1']=[1,2,3]

print("Value of key1:",dict['key1'])