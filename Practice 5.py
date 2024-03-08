Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruit=["Mango","Banana","Apple","Jackfruit","Watermelon"]
foods=["Rice","Milk","Fish","Egg","Chicken"]
AddList=fruit+foods
print(AddList)
['Mango', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken']
Addlist1Part=fruit+"Rice"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Addlist1Part=fruit+"Rice"
TypeError: can only concatenate list (not "str") to list
len(AddList)
10
"Pineapple" in AddList
False
"Apple" in AddList
True
AddList[0]='Lychee'
>>> print(AddList)
['Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken']
>>> print(AddList[-1])
Chicken
>>> print(AddList[0])
Lychee
>>> print(AddList[0:])
['Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken']
>>> print(AddList[:11])
['Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken']
>>> print(AddList[0:6])
['Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice']
>>> AddList.append("Onion")
>>> print(AddList)
['Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken', 'Onion']
>>> AddList.insert(0,"Mango")
>>> print(AddList)
['Mango', 'Lychee', 'Banana', 'Apple', 'Jackfruit', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken', 'Onion']
>>> AddList.insert(5,"Pineapple")
>>> print(AddList)
['Mango', 'Lychee', 'Banana', 'Apple', 'Jackfruit', 'Pineapple', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken', 'Onion']
>>> len(AddList)
13
>>> AddList[2]=
SyntaxError: incomplete input
>>> AddList[2]=''
>>> print(AddList)
['Mango', 'Lychee', '', 'Apple', 'Jackfruit', 'Pineapple', 'Watermelon', 'Rice', 'Milk', 'Fish', 'Egg', 'Chicken', 'Onion']
