#Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that
# find out,
list=[2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
extra=list[1]-list[0]
print(f"In Feb, {extra} dollars you spent extra compare to January")


#2. Find out your total expense in first quarter (first three months)
#of the year.
total=0
for i in list[0:3]:
    total= total+i
t=total
print("Total expense in first quarter (first three months) "
          "of the year is:", t)


#3. Find out if you spent exactly 2000 dollars in any month
if list[0:5]==2000:
    print("You spent exactly 2000 dollars in any month")
else:
    print("You didn't spent exactly 2000 dollars in any month")
#print("Did I spent 2000$ in any month? ", 2000 in list)


#4. June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list
list.append(1980)
print("With June Month, my expense is",list)


#5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense
# list based on this
bonus= list[3]-200
list[3]=bonus
print("After correction of April expense, the expense list is:", list)