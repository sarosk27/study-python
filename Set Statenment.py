#Set Statenment

names={'Ram','Sam','Ravi'}
print(names)
print(type(names))

print("----------------------------")

# Access Values Using For loop
print('Access Values Using For loop')
for name in names:
    print(name)

print("----------------------------")

# Adding New Element
print('Adding New Element')
names.add('Sara')
print(names)

print("----------------------------")
# Update Another Set of Data
print('Update Another Set of Data')
a={'Kumar','Sundar','Suresh'}
names.update(a)
print(names)

print("----------------------------")

#Remove the word or element 
#if the name was no in set 
#The Error message was appear
print('Remove the word or element \n if the name was no in set \n the Error message was appear') 
names.remove('Sara') 

print(names)

print("----------------------------")
#Discard is very Useful 
# the "Elenent" was not in set means it DO Nothing in set
print('#Discard is very Useful \n the "Elenent" was not in set means it DO Nothing in set')
names.discard('Suresh')
print(names)

print("----------------------------") 
print("pop")
names.pop()
print(names)
print('clear the SET')
names.clear()
print(names)
print('Delete the set completely')

'''


names={'Ram','Ram','Sam','Ravi','Kumar','Sundar','Suresh'}
del names
print(names)


'''
del names
names={'Ram','Ram','Sam','Ravi','Kumar','Sundar','Suresh'}
print(names)

print("----------------------------") 

a = {1, 2, 3, 4}
b = {'a', 'b', 'c', 'd'}
c=a.union(b)
print('union',c)
a.update(b)
print("update",a)

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

c=a.intersection(b)
print("intersection",c)

a.intersection_update(b)
print("intersection_update",a)

c=a.symmetric_difference(b)
print("symmetric_difference",c)

a.symmetric_difference_update(b)
print("symmetric_difference_update",a)
a = {1,2,3,4,5}
b = {5,6,7,8,9}


print('\tisdisjoint means set A and B \n\thave a different value va nu check pannum')
print('\tset A and B have same value "5" so ithu disjoint illa')
c=a.isdisjoint(b)
print("isdisjoint",c)

a={1,2,3}
b={1,2,3,4,5,6}

print('set A kulla values yallam set B kulla iruka nu check pannum')
c=a.issubset(b)
print("issubset",c)

a={1,2,3,4,5,6}
b={1,2,3,6}
c=a.issuperset(b)
print("issuperse",c)