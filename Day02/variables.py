name = "Raneya"
age = 17
country = "Pakistan"

print (name)
print (age)
print (country)

# Getting input from the user

name = input("What is your name? ")
age = int(input("What is your age? "))
country = input("What is your country? ")

#the comma tells print() to display both pieces of information with a space in between.
print("Hello, " + name + "!")
print("You are " + str(age) + " years old.")
print("You are from " + country + ".")

# Checking data types

print(type("Raneya"))  # Output: <class 'str'>
print(type(17))        # Output: <class 'int'>
print(type(5.8))       # Output: <class 'float'>
print(type(True))      # Output: <class 'bool'>


age = input("How old are you? ")
print(int(age) + 1)  # This will raise an error because age is a string, not an integer.

age = int(input("How old are you? "))
print(age + 1)  # This will work correctly because age is now an integer.

# int() means convert to integer, float() means convert to float, str() means convert to string, and bool() means convert to boolean.
number = int("25")  # Converts the string "25" to the integer 25

print(number)  # Output: 25
print(type(number))  # Output: <class 'int'>