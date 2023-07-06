#Nested If statenment
"""
3 mark input
Total
Average
Result
    If pass Grade
    90 - 100 A
    80 - 89  B
    70 - 79  C
    Else     D
"""
m1=int(input('Enter Tamil Mark '))
m2=int(input('Enter English Mark '))
m3=int(input('Enter Maths Mark '))
print("\n",m1,'Tamil\n',m2,'English\n',m3,'Maths\n', )
total=m1+m2+m3
average=total/3.0
print("Total Marks",total)
print("Average Marks",average)
if m1>=35 and m2>=35 and  m3>=35:
    print('Result : Pass ')
    if average>=90 and average<=100:
        print('Grade : A')
    elif average>=80 and average<=89:
        print('Grade : B')    
    elif average>=70 and average<=79:
        print('Grade : C')  
    else:
        print('Grade : D')
else:
    print('Result : Fail')
    print('Grade  : No Grade')


