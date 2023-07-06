#Identity Operators
"""
is 
is not
"""

a=[1,2]
b=[1,2]
c=a
print(id(a))
print(id(b))
print(id(c))

print("\n",a is c)
print(a is b)  #because of the value locationn is different
print(a==b)

print("\n",a is not b)
print(a  is not c)
print(a != b) #in this case a = b  so its False
