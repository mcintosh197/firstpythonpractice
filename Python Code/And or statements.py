'''
And statement
'''
age = int(input("What is your age?"))

if age < 2 :
    print("You can drink milk")
elif age >= 5 and age < 18:
    print("You can drink soda")
elif age >= 18 and age < 110:
    print("You can drink beer")
else:
    print("Invalid input")

'''
or statement 
'''
if age <= 5 or age >=65 :
    print("You qualify for a vaccine")
else:
    print("You're not qualified for the vaccine")
