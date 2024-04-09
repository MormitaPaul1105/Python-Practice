#After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
time = 0
for i in result:
    h = "heads"
    if h in i:
     time=time+1
    else:
        continue

print(f"{time} times I got heads")





