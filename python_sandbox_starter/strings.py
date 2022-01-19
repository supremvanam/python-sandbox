# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "Suprem"
age = 25

# Concatenate
print("Hello, my name is " + name + " and I am " + str(age))

# String Formatting

# Arguments by position
print("My name is {n}, {a} years old".format(n = name, a = age))

# f-strings
print(f"Hello this is {name} and I am {age}")

# String Methods

s = "helloworld"

print(s.split())

print(s.isalnum())

