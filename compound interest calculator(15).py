# Python compound interest calculator

#principle = float(input("Enter the principal amount: "))
#principle = 1
#rate = 0.05
#n = 2
#t = 2
#final_amount = principle*(1 + rate/n)**t
#print(final_amount)

#principle=0
#rate=0
#n=0
#time=0
#while principle<=0:
 #   principle=float(input("Enter the principle amount: "))
  #  if principle<=0:
   #     print("principle cannot be less than or equal to zero")
#while rate<=0:
 #   rate=float(input("Enter the rate amount: "))
  #  if rate<=0:
   #     print("rate cannot be less than or equal to zero")
#while time<=0:
 #   time=float(input("Enter the time taken in years: "))
  #  if time<=0:
   #     print("time cannot be less than or equal to zero")
#total = principle*(1 + rate/100)**time
#print(f"Balance after {time} year/s: ${total:.2f}")

"""break is used for breaking from a loop, we will learn more in for loops"""

principle=0
rate=0
time=0
while True:
    principle=float(input("Enter the principle amount: "))
    if principle<0:
        print("principle cannot be less than zero")
    else:
        break
while True:
    rate=float(input("Enter the rate amount: "))
    if rate<0:
        print("rate cannot be less than zero")
    else:
        break
while True:
    time=float(input("Enter the time taken in years: "))
    if time<0:
        print("time cannot be less than zero")
    else:
        break
total = principle*(1 + rate/100)**time
if time == 0 or time > 1:
    print(f"Balance after {time} years: ${total:.2f}")
else:
    print(f"Balance after {time} year: ${total:.2f}")