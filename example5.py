s1="MUNEEBA MEHMOOD"

print(len(s1))

x=0
while x<len(s1):
    #if s1[x ]!= 'A' and s1[x ]!= 'O' and s1[x ]!= 'E' : 
    if(s1[x] not in 'AEIOU'):
     print(s1[x])
    x=x+1

print("end")