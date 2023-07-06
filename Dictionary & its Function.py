#Dictionary & its Function
#Its have a "KEY" and "VALUES"

user={ "name":"sara", "age":21, "Is married":True }

print(user)
print(type(user))
print(user["name"])
print("\n\tusing 'get' fuction use panneum ptint panalam")
print(user.get("name"))

print(user.keys())
print(user.values())

print('\n\tprint the Holl set function')
print(user.items())




user={ 
    "name":"sara", 
    "age":21, 
    "Is married":True 
    }
print("\n---------------------------------") 

print('\nIn this case "X" Value is 1')
print('\n"USER" Value is 3 because of set range is 3') 



for x in user:
    print("\n user ",user)

print("\n---------------------------------") 

for x in user:
    print("\n x ",x)

print("\n---------------------------------") 

for i in user:
    print("\n",i," ", user[i])

print("\n---------------------------------") 
print("\nTo print the Values Only")
 
for x in user.values():
    print(x)

print("\n---------------------------------") 
print("\nTo print the Keys Only")
 
for x in user.keys():
    print(x)

print("\n---------------------------------") 
print("\nTo print the Items Only")

for x,y in user.items():
    print(x,y)

print("\n---------------------------------") 
if "age" in user:
    print("Present",)
    print(user["age"])

if "gender" in user:
    print("present", )
else:
    print("Gender Not Present",)
print("\n---------------------------------") 

#Change the Values
print("Change the Values")
user.update({"gender":"male"})
print(user)
print("\n---------------------------------") 
print("\n\tchange the particulat values 21 change into 35")
user["age"]=35
print(user)
print("\n---------------------------------") 
print("\n\tRemove the particulat Key the 'age' is removed ")
user.pop("age")
print(user)
print("\n---------------------------------") 
user.clear()
print(user)
print("\n---------------------------------") 

users={
        "user 1":{ 
                "name":"sara", 
                "age":21, 
                "Is married":True 
        }, # comma (,) is important 
        "user 2":{ 
                "name":"saraha", 
                "age":22, 
                "Is married":False 
        }
    }
print(users)