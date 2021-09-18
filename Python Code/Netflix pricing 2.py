'''
Netflix pricing using multiple choice
Using \n to make multiple choice
Using and if statement to get that choice
'''

hd_or_4k = input("Would you like HD or 4K?\n"
                 "Enter choice here: ").casefold().strip()

if hd_or_4k == "hd":
    options_hd = input("Please choose an option from below:\n"
                       "Option A: 1 User (HD): $5.99\n"
                       "Option B: 2 Users (HD): $7.99\n"
                       "Option C: 4 Users (HD): $10.99\n"
                       "Enter choice here: ").casefold().strip()
    if options_hd == "a" or options_hd == "1":
        print("You have choose option a you will be charged $5.99")
    elif options_hd == "b" or options_hd == "2":
        print("You have choose option a you will be charged $7.99")
    elif options_hd == "c" or options_hd == "3":
        print("You have choose option a you will be charged $10.99")
    else:
        print("You have not choose one of the three options")
elif hd_or_4k == "4k":
    options_4k = input("Please choose an option from below:\n"
                       "Option A: 1 User (HD): $7.99\n"
                       "Option B: 2 Users (HD): $9.99\n"
                       "Option C: 4 Users (HD): $13.99\n"
                       "Enter choice here: ").casefold().strip()
