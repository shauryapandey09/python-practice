# #input() = A function that prompts the user to enter data
# #              Returns the entered data as a string

#name = input("What is you name?:")
#age = int(input("How old are you?"))
##age = int(age), cuz input stores str values so we need to change it
#age += 1
#print(f"Hello {name}!")
#print("HAPPY BIRTHDAY")
#print(f"You are {age} years old.")

##Exercise 1: To find the area of a rectangle using input of user
#length = float(input("Enter the length of the ractangle: "))
#width = float(input("Enter the width of the ractangle: "))
#area = length * width

#print(f"The area of the ractangle is: {area}cm²") # superscript(²)--> Numlock + Alt + type 0178

##Exercise 2: Shopping cart program
#item = input("What item would you like to buy?")
#price = float(input("What is the price of the item?"))
#quantity = int(input("Please enter your quantity"))
#total = price * quantity
#if quantity == 1:
    #print(f"You have bought {quantity}x {item}")
#else:
    #print(f"You have bought {quantity}x {item}s")

#print(f"You total is ${total}")

#Exercise 3: Madlibs game
# word game where you create a story
# by filling in blanks with random words

adjective1 = input("Enter an adjective(description):")
noun1 = input("Enter a noun(person, place or thing):")
adjective2 = input("Enter an adjective(description):")
verb1 = input("Enter a verb(action)(ending with -ing):")
adjective3 = input("Enter an adjective(description):")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}")
