#If Else Statenment
"""
write a program to check Vote eligibility by enter his/her Name and age
"""
name=input('Enter your Name ')
age= int(input('Enter your Age'))
print('Your name ',name)
if age>=18:
    print(age,'your are eligiable to put your Vote')
else:
    print(age,'Your are not eligiable to put your vote')