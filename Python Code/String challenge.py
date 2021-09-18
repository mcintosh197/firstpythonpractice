'''
Concatenating a string
'''

name = input("What is your name? ")

print("Hello " + name.lower() + ", would you like to learn some Python today")

'''
Changing the case to upper
'''

name_change_case = input("What is your name? ")

print("Hello " + name_change_case.upper() + ", would you like to learn some Python today")

'''
Changing the case to title and string repeating
'''

name_change_case = input("What is your name? ").casefold().strip()

print(("Hello " + name_change_case.title() + ", would you like to learn some Python today?" + "\n") *3)
