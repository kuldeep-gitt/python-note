#map
def cube(num):
    return num**3

print(list(map(cube,[1,2,3,4,5])))
list1 = ['1','2','3','4','5']
for i in map(int,list1):
    print(i)

#filter
def even(num):
    return num%2==0

list2= [1,2,3,4,5,6]
print(list(filter(even,list2)))