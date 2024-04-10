# You are given following list of stocks and their prices in
# last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
dic_list={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}



#Write a program that asks user for operation. Value of operations
# could be,
text='''There are 2 options. Which one you want to choose?

a)print: When you enters "print" it should print list of stocks and their prices in last 3 days
b)add: When you enters 'add', it asks for stock ticker and price. '''
print(text)
user=input("Please enter print/add :")





#print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
if user=="print":
    for dic, value in dic_list.items():
        s=0
        for list in dic_list[dic]:
            s=s+list

        print(f'{dic}==>>{value}==> avg: {s/(len(value))}')






#add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then
# it will append the price to the list. Otherwise it will create
# new entry in your dictionary. For example entering
# 'tata' and 560 will add tata ==> [560] to the dictionary of
# stocks.
if user=="add":
    s=input("Please enter stock ticker:")
    p=int(input(f'Please enter {s} stock ticker price:'))
    if s in dic_list:
        dic_list[s].append(p)
        print(f'{s} stock ticker was already exist and your price is added in this list and updated list is:\n{s}==>{dic_list[s]}')

    else:
        dic_list[s]=[p]
        print(f"{s} stock ticker wasn't exist and created new entry in your dictionary and updated dictionary is:\n{dic_list}" )


