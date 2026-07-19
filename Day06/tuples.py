# Day 6 - Tuples

colors = ("red", "green", "blue")

print(colors) # stores 3 values
print(colors[0]) # gives the first term
print(colors[-1]) # gives the last term
print(colors[0:2]) # gives a slice

# Example tuple unpacking

student = ("Raneya", 17, "Pakistan")

name, age, country = student

print(name)
print(age)
print(country)

# Another example

coords = (5, 10)

x,y = coords

print(x)
print(y)