print ("=" * 40)
print ("Student Profile & Study Planner")
print ("=" * 40)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
study_hours = float(input("Enter the number of hours you study per day: "))

hours_per_year = study_hours * 365
next_year_age = age + 1

print("\nStudent Profile:")
print("Name: " + name)
print("Age: " + str(age))
print("Country: " + country)

print("\n==== Study Planner ====")
print("Next year, you will be " + str(next_year_age) + " years old.")
print("You will study " + str(hours_per_year) + " hours per year.")

# ==================== NOTES FOR IMPROVEMENT ====================

# 1. Use float() instead of int() when the user might enter decimal values.
# Example: Study hours can be 2.5 or 3.75, so float() is a better choice.

# 2. Prefer using commas in print() instead of string concatenation (+).
# Example:
# print("Age:", age)
# instead of
# print("Age: " + str(age))
# This is cleaner and Python automatically handles different data types.

# 3. Keep the formatting of headings consistent throughout the program.
# Use the same style for all sections to make the output look professional.

# 4. Add more user information to make the program more useful.
# Examples:
# - Favorite subject
# - Dream university
# - Favorite programming language

# 5. Add more calculations to make the project more interesting.
# Calculate:
# - Hours studied per week
# - Hours studied per month
# - Hours studied per year

# 6. Always choose meaningful variable names.
# Good examples:
# study_hours, hours_per_year, next_year_age

# 7. Before running the program, predict the output.
# This improves your logical thinking and debugging skills.

# 8. Write code that is easy to read.
# Good code is not only correct—it is also clean and understandable.

# ===============================================================