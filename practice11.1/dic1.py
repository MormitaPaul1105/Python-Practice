# We have following information on countries and their population (population is in crores),

# Country	Population
# China	       143
# India	       136
# USA	        32
# Pakistan	    21
# Using above create a dictionary of countries and its population
dic_countries={"China":143,"India":136,"USA":32,"Pakistan":21 }


# Write a program that asks user for three type of inputs,
text='''there are 3 types of input. Which one you want to choose?

a) print: if you enter "print" then it should print all countries
b)add: if you input "add" then it should further ask for a country name to add.
c)remove: when user inputs "remove" it should ask for a country to remove.
'''
print(text)




# a) print: if user enter print then it should print all countries with
# their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
user=input("Please enter print/add/remove :")
for dic in dic_countries:
    if user== "print":
        print(f'{dic}==>{dic_countries[dic]}')



# b)add: if user input add then it should further ask for a country
# name to add. If country already exist in our dataset then it should
# print that it exist and do nothing. If it doesn't then it asks for
# population and add that new country/population in our dictionary and
# print it
if user== "add":
   c_add= input("Please enter a country name to add:")
   if c_add in dic_countries:
       print(f'{c_add} exist and do nothing')
   else:
       p_add=int(input("Please give population of this country:"))
       dic_countries[c_add]=p_add
       print(dic_countries)


# remove: when user inputs remove it should ask for a country to remove.
# If country exist in our dictionary then remove it and print new
# dictionary using format shown above in (a). Else print that country
# doesn't exist!
if user=="remove":
    c_remove = input("Please enter a country name to remove:")

    if c_remove in dic_countries:
         del dic_countries[c_remove]
         for dic in dic_countries:
            print(f'{dic}==>{dic_countries[dic]}')
    else:
         print(f"{c_remove} country doesn't exist!")




# query: on this again ask user for which country he or she wants to query.
# When user inputs that country it will print population of that country.
user=input("Which country you wants to query:")
if user in dic_countries:
    print(f'The population of {user} country is: {dic_countries[user]}')
else:
    print("This country isn't found")

