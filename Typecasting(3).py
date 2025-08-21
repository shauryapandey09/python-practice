##Typecasting is the process of converting a variable from one data type to another
##           str(), int(), float(), bool()

#name = "Shaurya Pandey"
name = " "
age = 15
gpa= 9.4
is_student = True
##type is used to identify the data type
#print(type(name))
#print(type(age))
#print(type(gpa))
#print(type(is_student))

#gpa = int(9.4)

#print(gpa)

#age = float(age)
#print(age)

#age = str(age) #same as taking "25" (under quotes)
#print(type(age))
##age += "1" #age = age + 1
#print(age)
##It adds the number as a character like: 15 + 1 = 151

name= bool(name)
print(name)
## If the str, int or float is empty then bool() is always false, but when it contains a something(even a space), then it gives True always
## Can be used for checking if a user has typed in their name, age or anything else
## If they skip, then we can re-promt them to do so.