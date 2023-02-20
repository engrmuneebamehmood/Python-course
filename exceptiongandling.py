print("Muneeba Mehmood")
a=50
b=20

try :
    if a<b:
     c=a+b
     print(f"sum of a +b = {c}")
    else:
      c=a+x
except Exception as e:
   print("I wa strying, but there comes an error , so now i am in execpt")
   print(f"This is the error that i found in try{e}")
else:
    print  ("Try is executed successfully")
finally:
   print("I am done finally")

print("end")

#try will run if there is no error
#execute will eun if there is error in try
#else will run when there is no error just like try
# finally will run in all cases