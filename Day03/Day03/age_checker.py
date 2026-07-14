print("=" * 40)
print("AGE CHECKER")
print("=" * 40)

age = int(input("Enter your age: ")) #Ask the user to input their age and convert it to an integer  

if age < 13:  #If this condition is true, execute the following block of code
    print("You are a child.")

elif age < 18:  #If the previous condition is false and this condition is true, execute the following block of code
    print("You are a teenager.")

elif age < 65:  #If the previous conditions are false and this condition is true, execute the following block of code
    print("You are an adult.")

else:  #If all previous conditions are false, execute this block of code
    print("You are a senior citizen.")