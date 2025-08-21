#using math module
import math

#x=3.9
#print(math.pi)
#print(math.e)
#result = math.sqrt(x)  #sqrt will find the positive square root of the num
#result = math.factorial(x)  #find the factorial of the number
#result= math.ceil(x)    #ceil will always round off the number UP to whole num
#result= math.floor(x)    #floor will always round off the number DOWN to whole num
#print(result)

##Exercise 1: To find the circumference of a circle
#radius= float(input("enter radius of the circle:"))
#circumference = 2 * math.pi * radius
#print(f"The circumference is: {round(circumference,2)}cm")

##Exercise 2: To find the area of a circle
#radius= float(input("enter the radius of the circle:"))
#area = math.pi * radius**2 #OR
#area = math.pi * pow(radius,2) #from math module
#print(f"The area of the circle is {round(area,2)}cm²")

##Exercise 3: To find the hypotenuse of a right angled triangle
a = float(input("enter side A"))
b = float(input("enter side B"))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Side C = {c}")