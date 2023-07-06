#Date and Time 

import datetime as dt  #assin the "datetime" as "dt" i can use "dt"

current_date= dt.date.today()
print("Cuttent date ", current_date)

new=dt.date(2001,10,27)
print("2001,10,27")
print("day :",new.day)
print("month :",new.month)
print("year :",new.year)

print("\n---------------------------------") 

t=dt.time(10,25,30,555)
print(t)
print("second : ",t.second)
print("minute : ",t.minute)
print("hour : ",t.hour)
print("microsecond : ",t.microsecond)


print("\n---------------------------------") 

current_time= dt.datetime.now()
print("current_time",current_time)

print("\n---------------------------------") 

current_dt= dt.datetime.now()
new_year= dt.datetime(2024,1,1)
different= new_year - current_dt
print("different b/t new year :", different)

print("\n---------------------------------") 

current_dt= dt.datetime.now()
print(current_dt)
s=current_dt.strftime("%A %B %d %Y")
print(s)

