#Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print
# "you didn't finish the race"
# If you reply "no" then it should continue and ask
# "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
c=0
for i in range(1,6):
    user=input("Are you tired? Say yes/no: ")
    if user=="yes":

        print(f"complete {i} km ")
        print("you didn't finish the race")
        break
    elif user == "no":
         c=i
if c==5:
    print(f" Congratulations!, You have completed {c} km")
