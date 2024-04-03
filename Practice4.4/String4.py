# 4. I have a string variable called s='ami 300 apple kheyechi'. This of course is a
# wrong statement, the correct statement is 'ami 6 singara kheyechi'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
x='ami 300 ta apple kheyechi'
x=x.replace('apple','singara')
x=x.replace('300','6')
print("Using two line replace:",x)

x='ami 300 ta apple kheyechi'
x=x.replace('apple','singara').replace('300','6')
print("Using single line:",x)