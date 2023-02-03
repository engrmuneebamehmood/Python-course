'''
for output, we use print, concatenate, format
'''
x=10
print("X:",x)
print("This is the value of x")

#BY COMMA, we can do multiple prints in  one line
#by default , new line ati hy
'''agr ek he line mein krna ho, tu 
we can use end keyword '''
a=3
b=4
print(a ,b)
print("A:"  ,end= "B:")


name="Muneeba Mehmood"
age=20
country="Pakistan"

'''By simple print methood'''

#print("My name is",name , ", I'm",age,"years old ,", "and I live in",country)

'''
By concatenate methood
we can also concatenate ,means we can add strings '''

#print("My name is "+name+  " and i live in"+country)

#print("My name is "+name+ " my age is"+(str(age))+ " and i live in"+country)

'''
By format methood, just put f before double quotes in print 
and in curcly braces, write your variable name
we can also use  format methood for multiple prints'''

print(f"My name is {name} and my age is {age} and i live in {country}")
