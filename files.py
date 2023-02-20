
 # w is a mode to write in a file
 # r is a mode to read file
 #a is a mode for append
 # r+ for read and write
#w+ for read and write

f= open("Mydemofile.txt", "w")
 #creating a textfile of name Mydemofile, it;s extension is txt

f.write("I am writing in my demo file") #writing into my file

for i in range(1,10):
     f.write(str(i)+ "\n")

#appending my file
f= open("Mydemofile.txt", "a")
f.write("I am gonna make some changes in my file")
for i in range(1,10):
     f.write( "\nMuneeba Mehmood \n")


#reading from file
f=open("Mydemofile.txt", "r")
print(f.read()) #reading by read function

print(f.read(10)) #reading 10 characters

print(f.readline()) #reading line by line

f.close()