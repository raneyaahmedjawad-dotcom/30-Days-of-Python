def rectangle_area(length, width):
    return length * width

length = float(input("Enter the length: "))
width = float(input("Enter the width"))

area = rectangle_area(length, width)

print(f"\nThe area of the rectangle {area}")