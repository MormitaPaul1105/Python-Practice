#Write a python program that can tell you if your sugar is
# normal or not. Normal fasting level sugar range is 80 to 100.
#1.Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print
# that it is normal
user=float(input("Please enter your fasting sugar level:"))
for sugar in range(80,101):
    if sugar==user:
        print("Your sugar level is normal")
        break
    elif user<=sugar:
        print("Your sugar level is low")
        break
    elif user >= 101:
        print("Your sugar level is high")
        break
