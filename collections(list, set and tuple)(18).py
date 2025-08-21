"""     collection = single " a variable used to store multiple values
#   List  = [] ordered and changeable, Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK, NO Duplicates
#   Tuple = () ordered and unchangeable, Duplicates OK, FASTER
#   Dictionaries = will be covered later                                """
#fruits = ["apple", "orange", "banana", "coconuts"]
# print(fruits)
# print(fruits[::-1])    ##can use the index operator just like we do with strings(0 is the 1st element)
                    ##if the element is not found in the collection then you'll run into index error
# print(len(fruits))  ##number of elements
# print("pineapple" in fruits)    ##returns bool format(false here)

# fruits[0] = "pineapple" ##cuz lists can be reassigned(changed)

# fruits.append("pineapple") ##add an element at the end of a list
# fruits.remove("apple")      ##remove an element from a list
# fruits.insert(0, "banana")  ##replaces the index with object/element
# fruits.sort()       ##displays the list in alphabetical order
# fruits.reverse()      ##displays the list in reverse of what they were originally placed in
# fruits.clear()         ##clear all the elements
#  print(fruits.index("banana"))    ##gives the index of the element(if that element is not there, we get an error
#  print(fruits.count("banana"))       ##gives no. of elements in the list(0 or positive no.)
#print(fruits)

# for fruit in fruits:
   # print(fruit)

#   print(dir(fruits))   ##to list the different methods that are available for a collection
#   print(help(fruits))
#for fruit in fruits:
    #print(fruit,end=" ")

"""SETS"""
#fruits ={"apple", "orange", "banana", "coconut"}

""" we can use len(), in, cannot use indexing methods as set is unordered
,we cannot change the values but can use .remove() or .add() on objects, we can clear too, 
we can remove the first element(.pop)(which is random) too"""
# fruits.remove("apple")
# fruits.add("mango")     ##if the element is already in, it does nothing(no duplicates in sets)
# fruits.pop()    ##removes the first element(which is random as set is unordered)\
#  print(fruits)

"""TUPLES"""
fruits = ("apple", "banana", "cherry")

"""dir(),help() (obv), len(), in, .index, .count"""

# print(fruits.index("apple"))    ##gives index
# print(fruits.count("apple"))    ##how many occurrences

#for fruit in fruits:
  #  print(fruit)