def greet():
    print("Hello!")
    print("Welcome to Python!")

greet()

#def means "define" and is used to create a function in Python. In this case, the function is named "greet" and when called, it prints a greeting message to the console.
#greet() is the function call that executes the code inside the greet function, resulting in the output of the greeting message.
#() are parentheses used to call the function and can also be used to pass arguments to the function if needed. In this case, no arguments are passed, so the parentheses are empty.
#: starts the block of code that belongs to the function definition. Everything indented under the function definition is part of the function's body and will be executed when the function is called.

# Functions with parameters

def greet(name):
    print("Hello,",  name)

greet("Raneya")
greet("Ali")
greet("Sarah")

