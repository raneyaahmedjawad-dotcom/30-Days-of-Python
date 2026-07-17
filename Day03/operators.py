# Day 3

num1 = 20
num2 = 6

print("Number 1:", num1)
print("Number 2:", num2)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Floor Division:", num1 // num2)
print("Exponentiation:", num1 ** num2)

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Comparison Operators

a = 15
b = 20

print("a =", a)
print("b =", b)

print("a == b:", a == b) #Is a equal to b?
print("a != b:", a != b) #Is a not equal to b?
print("a < b:", a < b) #Is a less than b?
print("a > b:", a > b) #Is a greater than b?
print("a <= b:", a <= b) #Is a less than or equal to b?
print("a >= b:", a >= b)  #Is a greater than or equal to b?


# Logical Operators - AND (Both conditions must be true), OR (At least one condition must be true), NOT (Reverses the result)

# AND Operator

age = 17
is_student = True

print(age >= 16 and is_student) #True, because both conditions are true

# OR Operator

age = 15
has_permission = True

print(age >= 18 or has_permission) #True, because one condition is true

# NOT Operator

is_logged_in = True

print(not is_logged_in) #False, because the condition is true, and NOT reverses it

age = 17
has_id = True
has_ticket = False

print(age >= 18 and has_id and has_ticket) #False, because not all conditions are true
print(age >= 18 or has_id or has_ticket) #True, because at least one condition is true
print
(not (age >= 18 and has_id and has_ticket)) #True, because the NOT operator reverses the result of the AND operation

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density
