students = []

while True:
    print("\n===== Attendance Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter atudent name: ")
        students.append(name)
        print(f"{name} added successfully!")

    elif choice == "2": 
        if len(students) == 0:
            print("No students added yet.")
        else:
            print("\nStudents Present:")
            for student in students:
                print("-", student)

    elif choice == "3":
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print(f"{name} removed successfully!")
        else:
            print("Student not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")