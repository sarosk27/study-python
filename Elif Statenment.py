#Elif Statenment
"""
Take a Book in a library to Return the book later 
1 to 5 days to charge 0.5 ruppes
1-5    0.5
5-10   1
10-30  5
> 30 Membership Cancel
"""
days = int(input('Enter the days '))
if (days==0):
     print(days,'You have to pay the amount 0 ruppes')

elif (days>=1 and days<=5):
    print(days,'You have to pay the amount 0.5 ruppes',days*0.5)

elif (days>5 and days<=10):
     print(days,'You have to pay the amount 1 ruppes',days*1)

elif (days>10 and days<=30):
     print(days,'You have to pay the amount 5 ruppes',days*5)

else:
     print(days,'Your Membership is Cancel')