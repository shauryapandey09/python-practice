##SOME USEFUL STRING METHODS:

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")
#result = len(name) ##for the length of a string(no. of characters)(including space)
#result = name.find("ya")   ##gives first position of character. Starts from zero eth position
                        ##eg- if I input-Shaurya Pandey, S is zeroeth position
#result = name.rfind("q")   ##gives last occurrence of the input(when same character is coming more than once)
## if python doesn't find any character it will return -1

#name = name.capitalize()   ##Capitalize the first letter of a word using this
#name = name.upper()        ##Capitalize all the letters
#name = name.lower()         ##turn all the letters into lower case format(Decapitalize😁)
#result = name.isdigit()     ##gives boolian format ans to whether the input contains ONLY digits or not
                            ## it gives True only when everything is only digits
#result = name.isalpha()     ##returns a boolian True or false depending if the string contains only alphabets
                        ##(even a space counts as a non-alphabet)
#result = phone_number.count("-")    ##will return as a int type count of no. of characters in a string

#phone_number = phone_number.replace("-", "")   ##it will replace the all the old characters with new characters
#print(phone_number)
#print(help(str))                         ##help(str) gives a comprehensive list of all the str methods
                        ##help() also gives guide to more stuff on python

##Exercise 1: Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")
username.find(" ")
if len(username) > 12:
    print("Username too long (username can't be more than 12 characters)")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")
