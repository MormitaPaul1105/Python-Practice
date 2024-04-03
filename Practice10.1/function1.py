#Problem1:Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height
def calculate_area( base,  height):
    base=float(base)
    height=float(height)
    area = (1 / 2) * base * height
    return area
b=float(input("Enter the base:"))
h=float(input("Enter the height:"))
triangle_area= calculate_area( b, h)
print("The triangle area is:",triangle_area)

