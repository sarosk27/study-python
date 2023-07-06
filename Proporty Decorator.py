#Proporty Decorator

class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.mesg= self.name + " is " + str(self.age)+ " Years ago"
        # using + symbol to concadinate

    @property

    def msg(self):
        return self.name + " is " + str(self.age)+ " Years ago"
    

o=user("SARA",21)
print(o.name)
print(o.age)
print(o.msg)

o.name=45
print(o.msg) #the age 45 can not be changed
