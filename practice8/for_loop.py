
n = int(input("Enter a positive integer: "))


number = 0

print("The range is:")
for i in range(1, n + 1):
    print(i)
    number += i


print(f"The sum of numbers from 1 to {n} is: {number}")
