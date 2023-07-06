#init method

class user:
    def __init__(self):
        print("Call When New Instance Created")
        #self.name=name
        #print('Name :',self.name)
    def printall(self,name):
        self.name=name
        print('Name :',self.name)

o=user()

o=user()
print(o.__dict__)
o.printall("sara")
print(o.__dict__)