def welcome_student(name, course):
    print("=" * 40)
    print("Welcome,", name)
    print("Course:", course)
    print("We hope you enjoy learning python!")
    print("=" * 40)

student_name = input("Enter your name: ")
student_course = input("Enter your course: ")

welcome_student(student_name, student_course)