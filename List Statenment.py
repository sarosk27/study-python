#List Statenment
"""
Sequence type 
Mutable
"""

a=[1,2,3,4,5,6]
print(a)
print(type(a))
a[0]=100
print(a)
print('Slicing')
print('total len',len(a))
print(a[1])
print(a[1])
print(a[-1])
print(a[2:5])
print(a[:5])
print(a[::])
print(a[::-1]) #Reverse the list

print('---------------------------')

a=[1,True,"SARA",27.18,[1,2,3,4]]
print(a)
print(type(a))
print(a[0]," Type is ",type(a[0]))
print(a[1]," Type is ",type(a[1]))
print(a[2]," Type is ",type(a[2]))
print(a[3]," Type is ",type(a[3]))
print(a[4]," Type is ",type(a[4]))
print(a[4][2])                      #list kulla list
print(a[4][3])                      #list kulla list

print('---------------------------')

a=[10,20,30,40,50]
print(a)
a.clear()
print(a)
a=[10,20,30,40,50,20,30,20]
b=a.copy()
print('Copy the value a to b ',b)
print(b.count(20))
print(b.index(30))
print(b.index(30,5))
print(max(b))
print(min(a)) 
print(a)
a.pop(0)            #Delete the 0th index of a
print(a)  
a=[1,2,3,4,5]
a.pop()             #Remove the Last Element
print('pop',a)                    
a=[10,20,30,40,50,20,30,20]
a.remove(20)        #Remove the Element using Value
print(a)
print("--------------------------------------")

names=["ram"]
print(names)
names.append('sam')
names.append('kumar')
print(names)
   #names.append(input("enter the name "))
print(names)
n1=['mano']
names.extend(n1)   #Adding to list using extend
print(names)
names.reverse()
print(names)       #Reverse the List using Reverse keyword
names.insert(0,"Zara") #To insert the Value where we want 

print("--------------------------------------")

print(names)
num=[5,7,6,1,2,8,4,]
num.sort()         #Arrange the Elements
print(num)

print('---------------------------------------')

print(list(range(5)))
print(list('saravana'))

n1=['Zara', 'mano', 'kumar', 'sam', 'ram'] 
n1.sort(reverse=True)      #Ascending Order " revers=True"
print(n1)

n1=['Zara', 'mano', 'kumar', 'sam', 'ram'] 
n1.sort(key=len)    #Sorting list using "lenght"
print(n1)