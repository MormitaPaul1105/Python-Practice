#Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#Write a program that asks user to enter two cities and it tells
# you if they both are in same country or not. For example if
# I enter mumbai and chennai, it will print "Both cities are in
# India" but if I enter mumbai and dhaka it should print
# "They don't belong to same country"
print("Please enter two cities name:")
x=input()
y=input()
if x in india and y in india:
    print("Both cities are in India")
elif x in pakistan and y in pakistan:
    print("Both cities are in Pakistan")
elif x in bangladesh and y in bangladesh:
    print("Both cities are in Bangladesh")
elif x in india or y in india:
    print("They don't belong to same country")
elif x in pakistan or y in pakistan:
    print("They don't belong to same country")
elif x in bangladesh or y in bangladesh:
    print("They don't belong to same country")
else:
    print(f"Sorry, I don't know which country {x} and {y} cities belongs")
