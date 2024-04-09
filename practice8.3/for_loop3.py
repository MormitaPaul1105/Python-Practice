#Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and
# program should tell you in which month that expense occurred.
# If expense is not found then it should print that as well.
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list=["January","February","March","April","May"]
user=int(input("Please enter the expense amount:"))

t = -1
for n in range(len(expense_list)):

    if user == expense_list[n]:
        t =  n
        break
if t==-1:
    print(f"{user} expense isn't found")

else:
    print(f"In {month_list[t]} month({t + 1}), your expense is:{expense_list[t]}")