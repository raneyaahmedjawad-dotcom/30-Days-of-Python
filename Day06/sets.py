# Create your first set

fruits = ("Apple", "Banana", "Orange")
 
print(fruits)

# Duplicate values

numbers = {1, 2, 3, 3, 2, 1, 5}

print(numbers)

# Output = {1, 2, 3, 5}

# Add an item

fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)

# Remove an item

fruits.remove("Banana")

print(fruits)

# Check if something exists

if "Apple" in fruits:
    print("Apple is available!")
else:
    print("Apple is not available.")

