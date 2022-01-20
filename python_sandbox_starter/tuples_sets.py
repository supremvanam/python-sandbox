# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a Tuple
fruits = ('Apples', 'Oranges', 'Grapes')

print(fruits)

print(fruits[1])
# del fruits
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {"Apples", "Oranges", "Mango"}

print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grapes")

# Remove from set
fruits_set.remove("Oranges")

print(fruits_set)