##while loop = execute some code WHILE some condition remains true

##eg-1:
#name = input("Enter your name: ")
#while name == "":
  #  print("You did not enter your name")
  #  name = input("Enter your name: ")       ##add a way to escape the infinite loop
#print(f"Hello {name}")

##eg-2:
#age = input("What is your age? ")

#while not age.isdigit() or int(age) < 0:
  #  print("Please enter a valid age")
  #  age = input("What is your age? ")

#print(f"{age} years old")

##eg-3:
#food = (input("Enter a food you would like to eat(Enter q to quit): "))
#while not food == "q":
 #   print(f"You like {food}")
 #   food = input("Enter another food you want to eat(Enter q to quit): ")
#print("bye")

##eg-4
#num = int(input("Enter a number between 1 and 10:"))
#while num < 1 or num > 10:
    #print(f"{num} is not valid")
    #num = int(input("Enter a number between 1 and 10:"))
#num = int(input(f"Your number is {num}"))




