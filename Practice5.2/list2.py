#You have a list of your favourite marvel super heros.
#heros=['spider man','thor','hulk','iron man','captain america']

heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,
# 1. Length of the list
print("Length of the list is:",len(heros))

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print("New list is:",heros)

#3. You realize that you need to add 'black panther' after 'hulk',
   #so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print("After removing 'black panther' from the list, the list is:",heros)
heros.insert(2,'black panther')
print("After adding 'black panther' before 'hulk', the list is:",heros)


#4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them
# with doctor strange (because he is cool).Do that with one line of
# code.
heros.remove('thor')
heros.remove('hulk')
heros.insert(1,'doctor strange')
print("New list is:",heros)
#heros[1:3]=['doctor strange']
#print(heros)



#5. Sort the heros list in alphabetical order (Hint. Use
# dir() functions to list down all functions available in list)
#temporary sort
sorted_heroes = sorted(heros)
print("Sorted heroes list in alphabetical order:", sorted_heroes)
#Permanent sort
# heros.sort()
# print(heros)


