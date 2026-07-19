# A list stores multiple values in one variable

fruits = ["Apple" , "Banana" , "Orange"]

print(fruits)

# lesson 2

fruits = ["Apple" , "Banana" , "Orange"]

#Lists start counting from 0 

print(fruits[0])
print(fruits[1])
print(fruits[2])

#Lesson 3 - Negative Indexing

print(fruits[-1])

#Lesson 04 - Changing Items

fruits = ["Apple" , "Banana" , "Orange"]

fruits[1] = "Mango"

print(fruits)

#Lesson 5 - Adding Items

fruits = ["Apple" , "Banana"] 

fruits.append("Orange")

print(fruits)

#Basic Slicing

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print(fruits[1:4])

#Output: ['Banana', 'Orange', 'Mango']
#How it works: fruits[1:4]