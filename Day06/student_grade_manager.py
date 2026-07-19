print("=" * 50)
print("STUDENT GRADE MANAGER")
print("=" * 50)

students = []
grades = []

while True:
    print("\n" + "=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Grade")
    print("4. Find Highest Grade")
    print("5. Search Student")
    print("6. Exit")
    print("=" * 50)

    choice = input("Enter your choice (1-6): ")

# Option 1 - Add Student
    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter student's grade: "))

        students.append(name)
        grades.append(grade)

        print(f"\n {name} added successfully!")

    # Option 2 - View Students
    elif choice == "2":

        if len(students) == 0:
            print("\nNo students have been added yet.")

        else:
            print("\n===== STUDENT RECORDS =====")

            for i in range(len(students)):
                print(f"{i + 1}. {students[i]} - {grades[i]}")

    # Option 3 - Calculate Average Grade
    elif choice == "3":

        if len(grades) == 0:
            print("\nNo grades available.")

        else:
            average = sum(grades) / len(grades)
            print(f"\n Average Grade: {average:.2f}")

    # Option 4 - Find Highest Grade
    elif choice == "4":

        if len(grades) == 0:
            print("\nNo grades available.")

        else:
            highest = max(grades)
            index = grades.index(highest)

            print('\n Top Student')
            print(f"Name : {students[index]}")
            print(f"Grade: {highest}")

    # Option 5 - Search Student
    elif choice == "5":

        search = input("Enter student name: ")

        if search in students:
            index = students.index(search)

            print(f"\n Student Found")
            print(f"Name : {students[index]}")
            print(f"Grade: {grades[index]}")

        else:
            print("\n Student not found.")

    # Option 6 - Exit
    elif choice == "6":
        print("\n Thank you for using Student Grade Manager!")
        break

    # Invalid Choice
    else:
        print("\n Invalid choice! Please enter a number between 1 and 6")