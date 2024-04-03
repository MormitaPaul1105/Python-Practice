# problem 2:Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_triangle( base,  height,  shape_type=0):
 base = float(base)
 height = float(height)
 triangle_area = (1 / 2) * base * height
 return triangle_area
def calculate_rectangle( length, width, shape_type=0):

    length= float(length)
    width= float(width)

    rectangle_area = length * width
    return rectangle_area


Text = '''There are 2 option:
    Press 1: To get triangle area
    Press 2: To get rectangle area
    '''
print(Text)
s = int(input("Please choose any preferred number:"))

if s == 1:
    b = float(input("Enter the base:"))
    h = float(input("Enter the height:"))
    print("The triangle area is:", calculate_triangle(b, h,s))
elif s == 2:
    l = float(input("Enter the length:"))
    w = float(input("Enter the width:"))
    print("The rectangle area is:", calculate_rectangle( l, w,s))
else:
    b = float(input("Enter the base:"))
    h = float(input("Enter the height:"))
    print("The triangle area is:", calculate_triangle(b, h,s))






