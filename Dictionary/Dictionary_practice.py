dict = {'Name': 'sam', 'Age': 22, 'Gender': 'Male'}
print("My name is :  ",dict['Name'])
print("\nMy Age is :  ",dict['Age'])
print("\nMy Gender is :  ",dict['Gender'])


#adding new element
dict['City'] = 'Guna'
print("\nMy City is :  ",dict['City'])


#updating an element
dict['City'] = 'Indore'
print("\nMy new City is :  ",dict['City'])

#deleting city entry 
del dict['City']

#deleting all entries
dict.clear()

dict1 = {'Name': 'sam', 'Age': 22, 'Gender': 'Male'}

#length of dict1
print("\nlength is :  ",len(dict1))


#using get
print("\nGender is :  ",dict1.get('Gender'))
print(dict1.get('Myself',"Doesn't Exists"))


'''
if(dict1.has_key('Gender')):
    print("It has this key attribute")
else:
    print("doesnt contain that")
'''
print("\nItems are : ",dict1.items())

print("\nKeys are : ",dict1.keys())

print("\nValues are : ",dict1.values())
