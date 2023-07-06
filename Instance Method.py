#Instance Method

class student:
    name="Saravana Kumar"
    age = 21
    
    def printall(self , Gender):  #self use panna instance method
        print('Name :',student.name)
        print('Age :',student.age)
        print('Gender :',Gender)


o=student()
o.printall(" ")
print("\n-------------------------------------")
student.printall(o,"male") #this old method to print 
print("\n-------------------------------------")
o.printall('Male') #New method to print the instance