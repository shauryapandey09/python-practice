##CONDITIONAL STATEMENTS--> EXERCISE
#CODE 1: to find the largest number out of given 3 numbers
"""
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print(f"{num1} is largest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is largest number")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is largest number")
else:
    print('Invalid input')      """
#METHOD 2:
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)

print(f"{largest} is the largest number")

"""

##PROGRAM 2:
"""
principle = int(input("Enter principle(in rs): "))
time = int(input("Enter time(in years): "))
if principle < 25000:
    rate = 5
else:
    rate = 8
SI = (principle * rate * time)/100
print(f"The Simple interest is {SI}")
"""

##PROGRAM 3: to find out whether given year is a leap year
"""
year = int(input("Enter the year: "))
if year % 4 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
"""

##PROGRAM 4:
"""
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
"""

##PROGRAM 5:
"""
salary = int(input("Enter your salary: "))
gender = input("Enter your gender:(M/F) ")
if gender == "M":
    if salary < 50000:
        bonus = (10/100)*salary
        print(bonus)
    else:
        bonus = (15/100)*salary
        print(bonus)
elif gender == "F":
    if salary < 50000:
        bonus = (20/100)*salary
        print(bonus)
    else:
        bonus = (25/100)*salary
        print(bonus)
else:
    print("Invalid input")
"""

##PROGRAM 6: to determine if input 3 angles can be used to form a triangle
"""
angle1 = int(input("Enter angle 1 (in degrees): "))
angle2 = int(input("Enter angle 2 (in degrees): "))
angle3 = int(input("Enter angle 3 (in degrees): "))
if angle1 + angle2 + angle3 == 180:
    print("YES! The given angles can be used to form a triangle")
else:
    print("NO!  The given angles cannot be used to form a triangle")
"""
##PROGRAM 7:
"""
height = float(input("Enter your height(in meters): "))
weight = float(input("Enter your weight(in kg): "))
BMI = weight / pow(height, 2)
if 0 < BMI < 18.5:
    print("You are underweight")
elif BMI <= 0:
    print("You don't exist")
elif 18.5 < BMI <= 24.9:
    print("You are normal")
elif 25 < BMI <= 29.9:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")
else:
    print("invalid input")
print(f"Your BMI is {round(BMI),2}")
"""

##PROGRAM 8: grade calculator
"""
marks_percent = float(input("Enter your marks percentage: "))
if marks_percent < 33:
    print("F")
elif 33 <= marks_percent < 44:
    print("E")
elif 44 <= marks_percent < 60:
    print("D")
elif 60 <= marks_percent < 75:
    print("C")
elif 75 <= marks_percent < 90:
    print("B")
elif 90 <= marks_percent < 100 :
    print("A")
elif marks_percent == 100:
    print("A+")
elif marks_percent > 100:
    print("You should try talking to people")
else:
    print("Invalid input")
"""

##PROGRAM 9:
"""
consumed_units = int(input("Enter the consumed electrical units: "))
if consumed_units <= 100:
    cost = consumed_units * 2
    print(f"The cost of {consumed_units} electrical units is Rs.{cost}")
elif 100<consumed_units<= 200:
    cost = 200 + (consumed_units * 3.5)
    print(f"The cost of {consumed_units} electrical units is Rs.{cost}")
elif 200<consumed_units<= 300:
    cost = 550 + (consumed_units * 7.5)
    print(f"The cost of {consumed_units} electrical units is Rs.{cost}")
elif 300<consumed_units:
    cost = 1300 + (consumed_units * 9)
    print(f"The cost of {consumed_units} electrical units is Rs.{cost}")
else:
    print("Invalid input")
"""
##PROGRAM 10:
# METHOD 1:
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
middle = (num1+num2+num3)-largest-smallest
print(f"{smallest}, {middle}, {largest} ")
"""
# METHOD 2:
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

numbers = [num1, num2, num3]
numbers.sort()
print(f"Numbers in ascending order: {numbers}")
"""

## FULL EXERCISE(2) WITH FOR LOOPS (HARD ONE):
##PROGRAM 1: to print table of a given number
"""
num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
"""

##PROGRAM 2: To find the value of X^Y:
"""
x = int(input("Enter a number: "))
y = int(input("Enter the power/exponent: "))
print(f"{x}^{y} = {x**y}")
"""

##PROGRAM 3: To find the value of X!:
"""
x = int(input("Enter a number: "))
fact = 1
for i in range(1,x+1):
    fact = fact * i
print(f"Factorial of {x} is {fact}")
"""

##PROGRAM 4: To find the largest number out of given n numbers
#METHOD 1:using lists and append(adding an element to a list) through input
"""
n = int(input("Enter how many numbers: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
print(f"The largest number out of the given {n} numbers is {max(numbers)}")
"""
#METHOD 2: using an original largest and updating it if num>largest
"""
n = int(input("Enter how many numbers: "))
largest = float(input("Enter the first number: "))  # take the first number as the starting largest
for i in range(2,n+1):
    num = float(input(f"Enter number {i}: "))
    if num > largest:   # update if we find a bigger number
        largest = num   #not num = largest or ur just overwriting the num with the old largest
print(f"The largest number out of the given {n} numbers is {largest}")
"""

##PROGRAM 5:To find the sum of 1 + x + x^2 + x^3 +...+x^(n-1)
"""
n = int(input("Enter till how many numbers: "))
x = int(input("Enter a number: "))
summ = 0

for i in range(n):  # i goes from 0 to n-1
   summ += x**i     # add x^i to summ repeating on loop 
                        and storing the value each time in summ
print(f"The sum of {n} numbers is {summ}")
"""

##PROGRAM 6: to print n terms of the Fibonacci series:
"""
n = int(input("Enter how many numbers: "))
a , b = 0 ,1
c= 0
count = 0   #The no. of terms completed(which pos. are we at)
print("The Fibonacci sequence is as follows:")
if n<0:
    print("Enter a positive integer")
if n==0:
    print("Enter a positive integer")
while count <= n:
    c = a + b
    a, b = b, c
    count += 1
    print(c,end=", ")
"""
##PROGRAM 7:making * pattern with only one print statement
"""
rows = int(input("Enter the number of rows: "))

for i in range(1,rows+1):
    print("*"*i)
"""
##PROGRAM 8:
"""
rows = int(input("Enter the number of rows: "))
num = 1

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num, end=" ")
        num += 1
    print()
"""

##PROGRAM 9:to check if the number is prime or not:
"""
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not prime")
else:
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
"""
##PROGRAM 10:reverse a given number
"""
given_num= input("Enter a number: ")
reversed_num = given_num[::-1]
print(f"{given_num} is {reversed_num} in reverse")
"""
##PROGRAM 11:checking if the word is a palindrome or not
"""
word1 = input("Enter a word: ")
word2 = word1[::-1]
if word1 == word2:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
"""

##PROGRAM 12: count the number of digits of a number
"""
num = input("Enter a number: ")
print(len(num))
"""

##PROGRAM 13:find the sum of all the digits of a number
"""
num = int(input("Enter a number: "))
sum = 0

while num>0:
    sum = sum + num%10      #loops this for each digit until finished
    num //= 10  #divides by 10 and removes the decimal part 
print(sum)
"""

#PROGRAM 14: to find sum of all even and odd digits of the number
"""
num= int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

while num>0:
    digit = num%10
    if digit%2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit
    num //= 10
print(even_sum)
print(odd_sum)
"""