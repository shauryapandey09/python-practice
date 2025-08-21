"""SHOPPING CART PROGRAM:"""

"""we cannot use tuples as they are unchanging and we need changing user input
    we cannot use sets as they are unordered(you could but lists is best)"""

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":     ##to temporarily make the user input lower case in case they type "Q"
        break
    else:
        foods.append(food)