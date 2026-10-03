students = {
    "student1": {
        "name": "Ali",
        "age": 17,
        "grade": "A"
    },
    "student2": {
        "name": "Sara",
        "age": 18,
        "grade": "A*"
    }
}

print(students)

# access information

print(students["student1"]["name"])
print(students["student1"]["grade"])

print(students["student2"]["name"])
print(students["student2"]["grade"])

# loop through it

print("\n==== ALL STUDENTS ====")

for student_id, information in students.items():
    print("\nStudent ID:", student_id)

    for key, value in information.items():
        print(f"{key.title()}: {value}")