#list is a data type
#to store multiple items
#list is represented by []


'''
Functions we used

1) append
2) insert
3) remove
4)  pop
5) del

'''

fruit_names =['apple','cherry','mango','grapes']
print(fruit_names)
print(type(fruit_names))
print(fruit_names[2])
fruit_names.append("orange")#it will add orange in the list at the end
fruit_names.insert(1,"orange")#adding orange at index 1
fruit_names.remove("cherry")

print(fruit_names)
fruit_names.pop()#will delete last item
print(fruit_names)

fruit_names.pop(3)#will delete index 3 item
print(fruit_names)

del fruit_names[1] #we can use del as well
print(fruit_names)


#we can use list constructor 
'''
marks=list((10,20,30,40))
print(marks)
print(marks[3])
marks[2]=100# updating by replacing 30 by 100
print(marks)
'''

