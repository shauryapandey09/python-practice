## format specifiers = {value:flags} format a value based on what flags are inserted

#.(number)f = round to that many decimal places(fixed point)    ##print(f"price1 is {price1:.2f}") ##returns decimal upto 2 digits in float format
# :(number) = allocate that many spaces         ##print(f"price1 is ${price1:10}") ##gives how many spaces the input can work with
# :0X = allocate that many spaces       ##print(f"price1 is ${price1:010}") ##returns the number zero padded(eg of zero padded- $0003.14159)
# :< = left justify         ##it aligns the text to the left(like we do in word)
# :> = right justify        ##it aligns the text to the right  ##by default all text is right aligned already
# :^ = center align         ##it aligns the text to the center
# :+ = use a plus sign to indicate positive value   ##any positive no. precedes with a positive sign while a negative no. precedes with a negative sign
# := = place sign to leftmost position  ##idk
# : = insert a space before positive numbers     ## {: } same as :+ but replaces the + sign with a space( ) everything else remains same
# :, = comma seperator          ##can be used to for separation of every 1000th position(converts no. into international system)

price1 = 3000.14159
price2 = 9253458723.65
price3 = 6783.34

print(f"price1 is ${price1:=}")
print(f"price2 is ${price2:=}")
print(f"price3 is ${price3:=}")