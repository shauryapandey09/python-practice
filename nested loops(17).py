"""nested loops = A loop within another loop (outer,inner)
                    outer loop:
                        inner loop:"""      #indented
"""for x in range(3):
    for y in range (1,10):      ##we need different counters for each loop
        print(y,end=" ")        ##normally every print statement end with a new line, but we can set that to something else
    print()"""

##Exercise: drawing a rectangle with inputted length and breadth and symbol

"""rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end=" ")
    print()"""
for x in range(3):  ##y gives some output like 123456789, now as range(3), and there is only 1 element, the loop makes the element repeat itself(i think)
    for y in range (1,10):
        print(y,end="")
    print()