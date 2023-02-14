#it is a data type
#it is represented by{}
#it is orderless, no duplicate

country_names={'pakistan', 'Turkey','Syria','Kashmir'}
print(country_names)
print(type(country_names))

print(len(country_names))
country_names.pop()
print(country_names)

fruits=set(("mango", 'banana','apple'))
print(fruits)

print('grapes' in fruits)#checking if grapes is in fruit set or not


fruits.add("orange")
print(fruits) #we can add 

fruits.remove('mango')
print(fruits)#we can remove

fruits.clear()#by calling clear function
print(fruits)