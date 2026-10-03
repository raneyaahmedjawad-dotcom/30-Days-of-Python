print("=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

student = {
    "name": "Raneya",
    "age": 17,
    "country": "Pakistan",
    "course": "Python"
}

# Print the dictionary
print("\nOriginal Dictionary:")
print(student)

# keys()
print("\nAll Keys:")
print(student.keys())

# values()
print("\nAll Values:")
print(student.values())

# items()
print("\nKeys and Values:")
print(student.items())

# get()
print("\nStudent Name:")
print(student.get("name"))

# update()
student.update({"grade": "A*", "city": "Gujranwala"})

print("\nAfter Update:")
print(student)

# pop()
student.pop("country")

print("\nAfter Removing Country:")
print(student)

# clear() example
temporary = {
    "A": 1,
    "B": 2,
    "C": 3
}

print("\nTemporary Dictionary:")
print(temporary)

temporary.clear()

print("After Clear:")
print(temporary)