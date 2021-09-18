'''
This program will tell you're defined as
'''

name = input("Enter your name here: ")
age = int(input("Enter your age here: "))

if age <= 2:
    print(f"{name} you're a baby")
elif age > 2 or age <= 4:
    print(f"{name} you're a toddler")