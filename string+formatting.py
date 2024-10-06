'''Python for Beginners #11
String Formatting'''

s='bitten'
r='tech'
a=1000.4233746327847836723
#With format function

#r will be printed after s because of indexing
print('subscribe {1} {0}'.format(r,s))

#With f specifier (Python >=3.6)
print(f"subscribe {s} {r}")

#Precision and Width of floating point numbers
print(f"{a:1.3f}")