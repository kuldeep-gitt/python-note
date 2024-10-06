list = [x for x in range(10)]
print(list)

list = [letter for letter in 'abcde']
print(list)

list = [x**2 for x in range(10)]
print(list)

list = [x for x in range(10) if x%2==0]
print(list)

list = [x if x%2==0 else 'odd' for x in range(10)]
print(list)

list= [x*y*z for x in range(1,3) for y in range(1,3) for z in range(1,3)]
print(list)

list = [[x*y for x in range(3)] for y in range(3)]
print(list)