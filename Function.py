#Function 
def wellcome():
    print("Welcome Sara")

wellcome()
wellcome()

# There are 10 Types of functions

# 1) No Return Type Without Argunment Function
# 2) No Return Type With Argunment Function
# 3) Return Type Without Argunment Function
# 4) Return Type With Argunment Function
# 5) Arbitary Argunment Function using (*)
     #using the * means we can pass the many argunment
# 6) KeyWord Argunment Function  
# 7) Arbitary Keyword Argunment Function using (**)
# 8) Default Parameter Function
# 9) Passing a List as an Argunment in Function
#10) Recursive Function
     #oru function  andha work a complete panrathuku 
     #thanna thaane Call pannuchu na adhu "Recursive function"



# 1) No Return Type Without Argunment Function
print("1) No Return Type Without Argunment Function")

def add():
    a=int(input("Enter the Value A : "))
    b=int(input("Enter the Value B : "))
    c=a+b
    print('Total ',c)
add()

print("\n---------------------------------") 
# 2) No Return Type With Argunment Function
print("2) No Return Type With Argunment Function")
def  sub(a,b):
    c=a-b
    print("Different :",c)
sub(25,6)

print("\n---------------------------------") 
# 3) Return Type Without Argunment Function
print("3) Return Type Without Argunment Function")
def mul():
    a=int(input("Enter the Value A : "))
    b=int(input("Enter the Value B : "))
    c=a*b
    return c
x=mul()
print("Multiplication :",x)

print("\n---------------------------------") 
# 4) Return Type With Argunment Function
print("4) Return Type With Argunment Function")
def  div(a,b):
    c=a/b
    return c
x=div(24,6)
print("Division : ",x)
 

print("\n---------------------------------") 
# 5) Arbitary Argunment Function using (*)
#using the * means we can pass the many argunment
print("5) Arbitary Argunment Function using (*)\nusing the * means we can pass the many argunment")

def class_10(*students):
    print(students)
    print("\n\ttype",type(students))
    for name in students:
        print(name," ",end="")

    for name in students:
        print(name)
class_10("Ram","Sam","Saro","Sara")


print("\n---------------------------------") 

# 6) KeyWord with Argunment Function 
print("6) KeyWord with Argunment Function ")
def message(name, age):
    print(name,"age is ", age)
message(52, "Sara") #The Name and Age was inter-Changed
message(age=21,name="Sara") #So We can use "keyword" assen the value


print("\n---------------------------------") 
# 7) Arbitary Keyword Argunment Function using (**)
print("7) Arbitary Keyword Argunment Function using (**)")

def biodate(**date):
    print(date)

biodate(name="Saraha",age=20,gender="Female")
print(type(biodate))

print("\n---------------------------------") 
# 8) Default Parameter Function
print("8) Default Parameter Function")

def user (name, city="Dindigul"):
    print(name," is from ",city)
user("Saro","Chennai")
user("Sara")

print("\n---------------------------------") 
#9) Passing a List as an Argunment in Function
print("9) Passing a List as an Argunment in Function")

def total(marks):
    return sum(marks)
print("\n\tTotal",total([1,2,3,4,5,6,7,8,9]))




print("\n---------------------------------") 
# 10) Recursive Function
print("10) Recursive Function")

#oru function  andha work a complete panrathuku 
#thanna thaane Call pannuchu na adhu "Recursive function"

'''
Example  Factorial 5 means
1* 2* 3* 4* 5= 120
'''
def factorial (x):
    if x ==1:
        return 1
    else:
        return(x*factorial(x-1))
    #a=factorial(int(input("Enter the value:")))
    #print("Factorial ", a)
print("FACTORIAL :",factorial(5))





print("\n---------------------------------") 
# 11) Lambda Function 
print("11) Lambda Function ")

c= lambda a:a+50
print(c(5))

c=lambda a,b :a*b
print(c(5,6))
