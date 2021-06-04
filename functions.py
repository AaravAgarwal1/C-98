#open function- open any file
#read() function- reads file
#by defalut read mode

a= open("abcd.txt") #r is read mode (default)
a.read()

#reads everyline

fileline=a.readline() 

for line in fileline:
    print(line)


#split()- splits every word in a string

introstring="Hello. My name is Aarav!"

word=introstring.split(",") #seperate words
print(word)

#def function creating custom functions

def greet(name):
    print("Hello"+name+" How are you!")

greet("Aarav")
