'''
Getting quotes form an index
'''

band_name = "T'Pau had a hit called, \nChina in your hands"

print(band_name)
print(band_name[0:4] + " " + band_name [23:])

'''
Comparing variables 
'''

user_name = input("What is your name? ").title().strip()

if user_name == "Doctor Who":
    print("Doctor Who? ")
else:
    print("Hello " + user_name + "!")
