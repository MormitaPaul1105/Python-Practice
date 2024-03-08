Bangladesh=["Mango","Jackfruit","litchi","Watermelon","Coconut"]
American=["Grapes","Blueberries","Cranberries","Strawberry","Bleak cherry"]
Italian=["Kiwis","Cherries","Apricots","Peach","Nectarine"]
fruit=input("Enter a fruit name:")
if fruit in Bangladesh:
    print("This is Bangladeshi fruit")
elif fruit in American:
    print("This is American fruit")
elif fruit in Italian:
    print("This is Italian fruit")
else:
    print("I don't know about this fruit name")