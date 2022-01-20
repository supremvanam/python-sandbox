#imports and variables
import collections
from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]


# ------------------------------------------ LIST ------------------------------------------

# create a list from the variable 'harry' using the split() method 
# of the string class and print it
list_exercise = harry.split()
print(list_exercise)

# use the append() method once to add 'Eastwood' to the end of the  list
# use the insert() method to add 'Clint' at the start of the  list
# use the remove() method to remove 'question' from the list
# use the extend() method to add 'Dirty' and 'Harry' to the end of the list
# print the final list

list_exercise.append("Eastwood")
list_exercise.insert(0, "Clint")
list_exercise.remove("question:")
list_exercise.extend(["Dirty", "Harry"])
print(list_exercise)


# use the sort() method to order the  list
# print the list
# use the reverse() method to reverse the list
# print the final list

list_exercise.sort()
print(list_exercise)
list_exercise.reverse()
print(list_exercise)


# write the statement to produced the following lines of output

## There are 2 do's in the list
## You can find "ask" at index 9 of the list
## There are 17 elements in the list

do_repetition = collections.Counter(list_exercise)["do"]

print(f"There are {do_repetition} do's in the list")
print(f'You can find "ask" at index {list_exercise.index("ask")} of the list')
print(f'There are {len(list_exercise)} elements in the list')

# ------------------------------------------ TUPLE ------------------------------------------

#create a tuple from the variable pm and print it
# pm = 'justin pierre james trudeau'

tuple_exercise = tuple(pm)
print(tuple_exercise)

# write the statement to produced the following lines of output

## There are 4 e's in the tuple                   #use the count() method
## You can find a at index 15 of the tuple        #use the index() method
## There are 27 elements in the tuple             #use the len() function


# print(tuple_exercise.count("e"))
print("There are " + str(tuple_exercise.count("e")) + " e's in the tuple")
print("You can find a at index " + str(tuple_exercise.index("a")) + " of the tuple")
print(f"There are {len(tuple_exercise)} elements in the tuple")

# use decomposition to print the first, second and the rest of the elements of your tuple
first_element, second_element, *remaining_elements = tuple_exercise
print(f"The first element is {first_element}")
print(f"The second element is {second_element}")
print(f"The remaining tuples are {remaining_elements}")

# use array-like indexing to print the third and fifth element of your tuple
print(f"The third element of this tuple is {tuple_exercise[3]}")
print(f"The third element of this tuple is {tuple_exercise[5]}")


# ------------------------------------------ SET ------------------------------------------

# create a set from the variable 'instructor' and print it
# instructor = 'narendra pershad'

