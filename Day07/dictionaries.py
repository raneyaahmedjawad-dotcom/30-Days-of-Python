# a dictionary stores data as key : value pairs

print("=" * 50)
print("INTRODUCTION TO DICTIONARIES")
print("=" * 50)

# Creating a dictionary
student = {
    "name": "Raneya",
    "age": 17,
    "country": "Pakistan",
    "course": "Python"
}

# Print the whole dictionary
print("\nOriginal Dictionary:")
print(student)

# Access values using keys
print("\nStudent Name:", student["name"])
print("Country:", student["country"])

# Add new data
student["grade"] = "A*"
student["city"] = "Gujranwala"

print("\nAfter Adding Grade and City:")
print(student)

# Update existing data
student["age"] = 18
student["course"] = "Python + Data Structures"

print("\nAfter Updating:")
print(student)

# Delete an item
del student["country"]

print("\nAfter Deleting Country:")
print(student)

print("\nProgram Finished Successfully!")

# expected output

==================================================
INTRODUCTION TO DICTIONARIES
==================================================

Original Dictionary:
{'name': 'Raneya', 'age': 17, 'country': 'Pakistan', 'course': 'Python'}

Student Name: Raneya
Country: Pakistan

After Adding Grade and City:
{'name': 'Raneya', 'age': 17, 'country': 'Pakistan', 'course': 'Python', 'grade': 'A*', 'city': 'Gujranwala'}

After Updating:
{'name': 'Raneya', 'age': 18, 'country': 'Pakistan', 'course': 'Python + Data Structures', 'grade': 'A*', 'city': 'Gujranwala'}

After Deleting Country:
{'name': 'Raneya', 'age': 18, 'course': 'Python + Data Structures', 'grade': 'A*', 'city': 'Gujranwala'}

Program Finished Successfully!