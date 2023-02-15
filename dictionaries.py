#to store key value pair
#it is also a data type
#it is represented by {}

person={
'Name' : 'Muneeba Mehmood',
'Age'  : '20',
'Country': 'Pakistan',

}

person['Country']='turkey' #updating
person.pop('Age')


person.update({'name': 'Mehmood'})

print(f"Details of a person{person}")
print(type(person))
print(person['Name'])# accessing only name 

days=dict({'name': 'monday',
           'type':'working',
           'hours':24
           })

print(days)

print('seconds ' in days)
print('type' in days)

allkeys=days.keys()#to seel all keys 
print(allkeys)

allvalues=days.values()# to see all values
print(allvalues)

keyvalue=days.items()# to see all key value pairs
print(keyvalue)