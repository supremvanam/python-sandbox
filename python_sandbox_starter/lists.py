# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5]
fruits = ["Apples", "Oranges", "Avacados", "Grapes", "Pears"]

# Use a constructor
numbers2 = list((6,7,8,9,10))

print(fruits[1])
print(len(fruits))
fruits.append("Mangos")
fruits.insert(2, "Strawberries")
fruits.sort()

print(fruits)