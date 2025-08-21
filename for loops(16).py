"""  for loops = execute a block of code a fixed number of times
     You can iterate over a range, string, sequence, etc."""

"""     FORMAT:
    for (some counter) in range(a,b)"""

""" where a is inclusive and b is exclusive in the range function(begin,end,step)"""

#count to 10
#for x in range(1,11,3):     #reversed the order of outputs
   # print(x)

#credit_card = "1234-4567-7890"
#for x in credit_card:
 #   print(x)            #outputs the str as separate characters


#for x in range(1,21):
   # if x == 13:
        #continue    ##to skip over an iteration(the process of executing a block of code repeatedly)
           #AND
     #   break        ##escape the loop after the condition or whatever                                                                    ## you can use continue
    #else:
    #    print(x)

"""while loops vs for loops
while= when you need to execute something possibly for infinite amount of times(eg- when you accept user input)
for = when you need to execute something for a fixed amount of times"""

##COUNTDOWN TIMER
import time
#time.sleep(x)       ##when executed, nothing happens for x seconds and then the code is executed.
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):      ##or reversed(range(0,my_time))
    seconds = x % 60     ##in our clock, we can't go over 60, so we place % sign(modulus)
    minutes = int(x/60) % 60
    hours = int(x/3600 % 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")