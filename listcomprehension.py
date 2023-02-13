numbers=[10,20,30,40,4,2,1,5,3,60]
even=[]
#t get list of only even numbers
'''
for x in numbers:
    if x%2 ==0:
        even.append(x)
print(even)
'''

#to create a list in single line by line comprehension
marks=[15,40,45,67,78,23,46,90]
for m in marks: 
#even_marks= [m for m in marks if m%2 ==0]
#print(even_marks)
    print(m*2)