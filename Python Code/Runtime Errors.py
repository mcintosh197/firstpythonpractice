'''
Runtime errors
'''

option = input("Select an option: A, B, C or D: ").strip()
meaning = ("Python")

if option.lower() == "a":
    print("Hello World!")

elif option.lower() == "b":
    print(1/1)

elif option.lower() == "c":
    print("you cannot add text and numbers " + str(12))

elif option.lower() == "d":
    print("The meaning of life is " + meaning)

else:
    print("You need to choose an option from the list A, B, C or D: ")