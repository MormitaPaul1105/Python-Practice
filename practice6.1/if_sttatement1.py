#Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#Write a program that asks user to enter a city
# name and it should tell which country the city belongs to

user=input("Please enter a city name:")

if user in india:
    print(f'{user} city belongs to India')
elif user in pakistan:
    print(f'{user} city belongs to Pakistan')
elif user in bangladesh:
    print(f'{user} city belongs to Bangladesh')
else:
    print(f"Sorry, I don't know which country {user} city belongs")



