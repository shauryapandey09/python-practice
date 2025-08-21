# if = Do some code only if some condition is True
#       Else do something else

#age = int(input("Enter an age: "))
##any code under the if statement should be indented(tab wali space honi chahiye)
#if age >= 100:                                  #Main condition
    #print("You are too old to sign up!")
#elif age < 0:                                   #Other conditions
    #print("You have not been born yet")
#elif age >= 18:                                 #Other conditions
    #print("You are now signed up!")
#else:                       #If all other conditions are false then this code is run
    #print("You must be 18+ to sign up!")


#response = input("Would you like food(Y/N)")

#if response == "Y":     #to check to see if two values are equal we use ==(compartive)
    ## = is the assignment operator while == means we are considering or comparing
    #print("Have some food")
#else:
    #print("No food for you")


#name = input("Enter your name: ")

#if name == "":
    #print("YOU DIDN'T TYPE YOUR NAME")
#else:
    #print(f"Hello {name}")

#online = True

#if online:
    #print("The user is online")
#else:
    #print("The user is offline")


##Exercise 1:Python Calculator

#operator = input("Enter an operator(+, -, *, /):")
#num1 = float(input("Enter the first number:"))
#num2 = float(input("Enter the second number:"))
#if operator == "+":
   # result = num1 + num2
   # print(round(result, 3))
#elif operator == "-":
   # result = num1 - num2
  #  print(round(result, 3))
#elif operator == "*":
  #  result = num1 * num2
  #  print(round(result, 3))
#elif operator == "/":
  #  result = num1 / num2
  #  print(round(result, 3))
#else:
    #print(f"{operator} is not a valid operator")


##Exercise 2: Python weight converter

#weight = float(input("Enter your weight:"))
#unit = input("Kilograms or Pounds? (K/L): ")

#if unit == "K":
    #weight = weight * 2.205
   # unit = "Lbs"
   # print(f"your weight is {round(weight, 1)} {unit}")
#elif unit == "L":
   # weight = weight / 2.205
   # unit = "Kgs"
   # print(f"your weight is {round(weight, 1)} {unit}")
#else:
    #print(f"{unit} is not a valid unit")


##Exercise 3: Temperature conversion program

#unit = input("Is this temperature in Celsius or Fahrenheit?(C/F):")
#temperature = float(input("Enter your temperature in Celsius or Fahrenheit:"))

#if unit == "C":
   # temperature = round((temperature * 9) / 5 + 32,1)
   # print(f"your temperature is {round(temperature, 1)} Fahrenheit")
#elif unit == "F":
   # temperature = round((temperature - 32) * 5 / 9,1)
  #  print(f"your temperature is {round(temperature, 1)} Fahrenheit")
#else:
    #print(f"{unit} is not a valid unit")


##A better way to code to check if the num is odd or even:
#Jr. Method:
#num = int(input("Enter a Number"))
#if num % 2 == 0:
   # print(f"{num} is an even number")
#else:
   # print(f"{num} is an odd number")

##Sr. Method:
num = int(input("Enter a number"))
print("Even" if num % 2 == 0 else "Odd")



