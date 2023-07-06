#class Attribute

class Student():
    name = "Sara"
    age = 21
 
 
''' This is Class Attributes '''
 
# getattr method
print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
print(getattr(Student, 'gender', 'No Such Attribute Found'))
 
# Dot Notation
print(Student.name)
print(Student.age)
 
# setattr
setattr(Student, 'name', 'Saro')
print(Student.name)
 
setattr(Student, 'gender', 'Male')
print(Student.gender)
 
Student.city = "Dindigul"
print(Student.city)
 
print(Student.__dict__)
delattr(Student,"city") 
print(Student.__dict__)
del Student.gender
print(Student.__dict__)
  