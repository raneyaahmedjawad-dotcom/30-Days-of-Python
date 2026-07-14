print("=" * 40)
print("GRADE CALCULATOR")
print("=" * 40)

marks = int(input("Enter your marks (0-100): ")) #Ask the user to input their marks and convert it to an integer

if marks < 0 or marks > 100: #If this condition is true, execute the following block of code
    print("Invalid marks. Please enter a value between 0 and 100.")

elif marks >= 90: #If the previous condition is false and this condition is true, execute the following block of code
    print("You got an A grade.")

elif marks >= 80: #If the previous conditions are false and this condition is true, execute the following block of code
    print("You got a B grade.")

elif marks >= 70: #If the previous conditions are false and this condition is true, execute the following block of code
    print("You got a C grade.")

elif marks >= 60: #If the previous conditions are false and this condition is true, execute the following block of code
    print("You got a D grade.")

else: #If all previous conditions are false, execute this block of code
    print("You got an F grade. Better luck next time!")
    