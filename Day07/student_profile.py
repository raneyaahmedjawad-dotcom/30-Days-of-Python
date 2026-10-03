student = {
    "name": "Raneya",
    "age": 17,
    "country": "Pakistan",
    "course": "Python",
    "grade": "A*"
}

print("=" * 40)
print("STUDENT PROFILE")
print("=" * 40)

for key, value in student.items():
    print(f"{key.title()}: {value}")

    