##indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]
#starting index is inclusive(included) but ending index is exlusive
#if u type [x:] python thinks that we need everything till the end of the str
#negative inverts the str(like -1 position would be 6 here)[-2:]= 56
#[::x] step returns the characters at every x no. of characters


#credit_number = "1234-5678-90123-3456"

#print(credit_number[4])     #position of character(any) starting from 0
#print(credit_number[0:4])   #returns the range of the positions together as a str
                             #starting index is inclusive(included) but ending index is exclusive
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-2:])
#print(credit_number[::3])

#last_digits = credit_number[-4:]

#print(f"xxxx-xxxx-xxxx-{last_digits}")
#credit_number = credit_number[::-1]     ##negative step reverses the str
#print(credit_number)

