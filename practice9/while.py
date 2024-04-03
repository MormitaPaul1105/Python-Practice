Text='''There are 2 option:
Press 1: For odd number sum
Press 2: For even number sum
'''
print(Text)

X=input("Choose your any one preferred number:")
X=int(X)
while X>=3:
 print("There are no number exist here")
 X = int(input("Choose your 1 or 2 number:"))
 continue

while X==1:
   y = int(input("Please take any odd number:"))
   if y % 2 ==0:
    print("You take wrong number which is even ")
    #y = int(input("Please take any odd number to get sum:"))
    continue

   print ("The range is:")
   so=0
   for i in range (X,y+1,2):
    print(i)
    so=so+i

   print(f"The sum of numbers from 1 to {y} is: {so}")
   break


while X==2:
    y = int(input("Please take any even number:"))
    if y % 2 !=0:
        print("You take wrong number which is odd ")
        #y = int(input("Please take any even number to get sum:"))
        continue

    print ("The range is:")
    se=0
    for i in range (X,y+1):
            if i % 2 != 0:
                continue
            print(i)
            se=se+i
    print(f"The sum of numbers from 2 to {y} is: {se}")
    break
