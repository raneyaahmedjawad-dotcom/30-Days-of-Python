print ("=" * 40)
print ("Student Profile & Study Planner")
print ("=" * 40)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
study_hours = int(input("Enter the number of hours you study per day: "))

hours_per_year = study_hours * 365
next_year_age = age + 1

print("\nStudent Profile:")
print("Name: " + name)
print("Age: " + str(age))
print("Country: " + country)

print("\n==== Study Planner ====")
print("Next year, you will be " + str(next_year_age) + " years old.")
print("You will study " + str(hours_per_year) + " hours per year.")

