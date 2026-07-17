print("=" * 40)
print("MULTIPLICATION TABLE")
print("=" * 40)

number = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11): #Loop through the range of numbers from 1 to 10
    result = number * i #Calculate the multiplication result
    print(f"{number} x {i} = {result}") #Print the multiplication table in a formatted way  
    