Text='''There are 4 types of area:
Press 1: For Triangle Area
Press 2: For Rectangle Area
Press 3: For Square Area
Press 4: For Circle Area'''
print(Text)

X=input("Choose your any one preferred area:")
X=int(X)
while X >= 5:
 print("There are no area exist in this number")
 X =int( input("Choose your any one preferred area:"))
 continue
while X<=4:

 if X==1:
    base = input("Enter base in meter:")
    base = float(base)
    height = input("Enter height in meter:")
    height = float(height)
    area1=0.5*(base*height)
    print("Your Triangle Area is:", area1)
    area1 = float(area1)
    if area1%2!=0:
        print("The area number is odd number")
    else:
        print("The area number is even number")
 elif X==2:
    base = input("Enter base in meter:")
    base = float(base)
    height = input("Enter height in meter:")
    height = float(height)
    area2 =(base * height)
    print("Your Rectangle Area is:", area2)
    area2=float(area2)
    if area2 % 2 != 0:
        print("The area number is odd number")
    else:
        print("The area number is even number")
 elif X == 3:
        base = input("Enter base in meter:")
        base = float(base)
        area3 = base**2
        print("Your Square Area is:", area3)
        area3 = float(area3)
        if area3 % 2 != 0:
            print("The area number is odd number")
        else:
            print("The area number is even number")
 elif X == 4:
        r = input("Enter radius in meter:")
        r = float(r)
        area4 = 3.1416*(r**2)

        print("Your Circle Area is:",area4)
        area4 = float(area4)
        if area4 % 2 != 0:
            print("The area number is odd number")
        else:
            print("The area number is even number")
 break
#else:
    #print("There are no area exist in this number")

