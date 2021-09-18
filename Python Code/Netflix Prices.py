'''
Netflix pricing using multiple choice
Using \n to make multiple choice
Using and if statement to get that choice
'''

choice = input("Please choose an option from below:\n"
               "Option A: 1 User (HD): $5.99\n"
               "Option B: 2 Users (HD): $7.99\n"
               "Option C: 4 Users (HD): $10.99\n"
               "Enter choice here: ").casefold().strip()

if choice == "a" or choice == "1":
    print("You have choose option a you will be charged $5.99")
elif choice == "b" or choice == "2":
    print("You have choose option a you will be charged $7.99")
elif choice == "c" or choice == "3":
    print("You have choose option a you will be charged $10.99")
else:
    print("You have not choose one of the three options")
