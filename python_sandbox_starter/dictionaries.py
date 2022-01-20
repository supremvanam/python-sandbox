# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    "first_name": "Suprem",
    "last_name": "Vanam",
    "age": "25"
}

print(person)

print(person['first_name'])
print(person.get("last_name"))

# Add a key-value
person["phone"] = "416-417-4898"

print(person.keys())