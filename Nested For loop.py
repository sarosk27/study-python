#Nested For loop
"""
*
**
***
****
*****

*****
****
***
**
*

A-Z ASCII Value is 65-90
a-z ASCII Value is 97-122

A
AB
ABC
ABCD
ABCDE

ABCDE
ABCD
ABC
AB
A

"""


for i in range(6):
    for j in range(i):
        #print("*")
        print("*", end="")   #end is used to print same line
    print("")
    

print("___________________________________")

for i in range(5,0,-1):
    
    for j in range(i):
        
        print("*", end="")    #end is used to print same line
        
    print("")

print("___________________________________")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j), end="")

    print("",)

print("___________________________________")

for i in range(5):
    for j in range(i+1):
        print(chr(65+j), end="")
    print("")

print("___________________________________")

for i in range(i,0,-1):
    for j in range(i):
        print(chr(65+j), end="")
    print("")
