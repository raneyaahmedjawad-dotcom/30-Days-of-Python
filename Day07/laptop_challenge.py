laptop = {
    "brand": "Dell",
    "ram": "16 GB",
    "storage": "512 GB SSD",
    "price": 180000
}

# Print all keys
print("Keys:")
print(laptop.keys())

# Print all values
print("\nValues:")
print(laptop.values())

# Print all items
print("\nItems:")
print(laptop.items())

# Add processor
laptop["processor"] = "Intel i7"

# Change the price
laptop["price"] = 175000

# Remove storage
laptop.pop("storage")

# Print final dictionary
print("\nFinal Dictionary:")
print(laptop)