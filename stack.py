# queue  first come firt serve
#stack first come last serve

stack=[]

while True:
    a=input("enter 1 to push \n enter 2 to pop \n enter 0 to exit")

    if a=='0':
        break

    elif a=='1':
       name=input("Enter item to push:")
       stack.append(name)

    elif a=='2':
        if len(stack) <=0:
         print("stack is already empty")
        else:
            x=stack.pop()
            print(f"popped item is {x}")
    else:
        print("Invalid")
    print(stack)



