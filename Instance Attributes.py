#Instance Attributes

class user:
    course = 'Java' #Instance Attributes
 
 
o = user()
#print("print a o",o)
print(user.__dict__)
print(user.course)  # Print Class attribute
print("o.__dict__",o.__dict__)
print(o.course)
o.course = "C++"
print("o.__dict__",o.__dict__)
print(o.course)
 
o2 = user()
print(o2.course)