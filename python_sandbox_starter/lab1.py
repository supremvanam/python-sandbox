#imports and variables
import collections
from operator import le
from random import randint

print("This is my practice file. Please review the colab link for assignment submission")
print("Colab Link: https://colab.research.google.com/drive/1RgSqX7fHT-8Jke8ac-9VdF-upYQ-k7T9?usp=sharing")


#the following variables will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]


print("------------------------------------------ LIST ------------------------------------------")

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

print("------------------------------------------ TUPLE ------------------------------------------")

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


print("------------------------------------------ SET ------------------------------------------")

# create a set from the variable 'instructor' and print it
# pm = 'justin pierre james trudeau'
# instructor = 'narendra pershad'

set_exercise = set(instructor)
comparision_set = set(pm)

# use the add() method to add 'z' to the set and print it
set_exercise.add("z")

#use the remove() method to take ' ' from the set and print it
set_exercise.remove(" ")

# use the intersection() method to find the common elements in both sets and print the result
print(set_exercise.intersection(comparision_set))

# use the union() method to find all the elements occuring in both sets and print the result
print(set_exercise.union(comparision_set))

#use the pop() method remove and return an arbitrary elements of the set and print it
print(set_exercise.pop())

#use the update() function to add 'x', 'y' and 'z' to the set  and print the result
print(set_exercise.update({"X", "Y", "Z"}))

print(len(set_exercise))

print(set_exercise)


print("------------------------------------------ DICTIONARY ------------------------------------------")

d = { 
    3462: 'Artificial Intelligence', 
    3468: 'Software Engineering Technician', 
    3469: 'Software Engineering Technology', 
    3472: 'Artificial Intelligence (FT)', 
    3478: 'Software Engineering Technician (FT)', 
    3528: 'Health Informatics Technology (FT)', 
    3609: 'Game - Programming', 
    3668: 'Health Informatics Technology', 
    3679: 'Game - Programming (FT)'
    }

print(d)

print(d.keys())
print(d.values())

print(d[3462])
print(d.get(3462))


print("------------------------------------------ ITERATING OVER A COLLECTION ------------------------------------------")

for set_item in set_exercise:
    print(set_item)

for tuple_item in tuple_exercise:
    print(tuple_item)

for dict_item in d:
    print(dict_item)


print("------------------------------------------ CONVERSIONS ------------------------------------------")

print("------------------------------------------ SET CONVERSIONS ------------------------------------------")

tuple_to_set = set(tuple_exercise)
list_to_set = set(list_exercise)
dict_to_set = set(d)

print(tuple_to_set)
print(list_to_set)
print(dict_to_set)

print("------------------------------------------ TUPLE CONVERSIONS ------------------------------------------")

set_to_tuple = tuple(set_exercise)
list_to_tuple = tuple(list_exercise)
dict_to_tuple = tuple(d)

print(set_to_tuple)
print(list_to_tuple)
print(dict_to_tuple)

print("------------------------------------------ LIST CONVERSIONS ------------------------------------------")

set_to_list = list(set_exercise)
tuple_to_list = list(list_exercise)
dict_to_list = list(d)

print(set_to_list)
print(tuple_to_list)
print(dict_to_list)


print("------------------------------------------ ENUMERATE FUNCTION ------------------------------------------")
print(list(enumerate(set_exercise)))
print(list(enumerate(tuple_exercise)))
print(list(enumerate(list_exercise)))
print(list(enumerate(d)))

print("------------------------------------------ PRINT POSITION, KEY, VALUE OF DICTIONARY ------------------------------------------")

for position, (key, value) in enumerate(d.items()):
    print(position, key, value)

