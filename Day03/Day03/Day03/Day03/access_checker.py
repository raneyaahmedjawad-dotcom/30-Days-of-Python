print("=" * 40)
print("ACCESS CHECKER")
print("=" * 40)

age = int(input("Enter your age: ")) #Ask the user to input their age and convert it to an integer

if age >= 18: #If this condition is true, execute the following block of code
    has_id = input("Do you have a valid ID? (yes/no): ").strip().lower() #Ask the user if they have a valid ID and convert the input to lowercase
    if has_id == "yes":
        print("You have access.")
    else:
        print("You do not have access.")
else:
    print("You do not have access.")