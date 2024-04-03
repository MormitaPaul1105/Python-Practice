street = "128/2 godown road"
city = "Lakshmipur"
country = "Banladesh"
address = street + '\n' + city + '\n' + country
print("Address using + operator:",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:",address)