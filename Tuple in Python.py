#Tuple in Python 
#Immutable
#Surrounded by Normal Braket ( )
#We "MUST BE USE (,) SYMBEL"
print("----------------------------")

a=(1)
print(a,type(a))
a=(1,)
print(a,type(a))

print("----------------------------")

a=(1,True,27.18,"saro")
print(a)
print(type(a))
print(a[3])
print(a[-4])

#We can't change the Tuple Element
#Incase we had to be change the Element means 
#We can convert the "TUPLE into LIST"
#And then we can convert "LISt into TUPLE"

b=list(a)
print(type(b))
print(b)

b.append("raja")
b.insert(0,"kumar")
print(b)

a=tuple(b)
print(type(a))
print(a)

print("----------------------------")

for i in a:
    print(i)

if "saro" in a:
    print("saro is found")
else:
    print('Not found')

print("----------------------------")

a=(1,2,3,4,5)
b=(6,7,8,9,10)
c=a+b     #Conjuction the Two Tuples
print(c)

c=(a,b)   #Nested Tuples   Tuples kulla Tuples
print(c)
print(c[0])
print(c[1])
print(c[0][1])
print(c[0][3])
print(c[1][0])
print(c[1][2])