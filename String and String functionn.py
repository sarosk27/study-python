#String and String functionn
s= "saravana kumar"
print(type(s))
print(len(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('a'))
print(s.count('a'))
print(s.endswith('ar'))
print(s.find('a'))
print(s.find('a',4))
print(s.replace('a','A'))

a= "SAROSK"
print('is upper ? ',a.isupper())
print('is lower ? ',a.islower())

b= "this \n is \n my \n things"
print(b)
print(b.splitlines())
print(b.splitlines(True))
print(b.split('\n'))
 
c="   saravana    "
print(len(c))
print('Remove the space ',c.strip())
print("remove only leftside space ",c.lstrip())
print('remoe the right side space ',c.rstrip())

d="27-10-2001"
print('seperate the month and year ',d.partition('-'))