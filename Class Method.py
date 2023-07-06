#Class Method

class student:
    name="Saravana Kumar"
    age = 21
    
    def printall():
        print('Name :',student.name)
        print('Age :',student.age)
student.printall()
print(student.__dict__)

print(getattr(student,'printall'))
getattr(student,'printall')()

student.__dict__['printall']()