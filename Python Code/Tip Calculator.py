'''
This a calculator to calculate the amount of tip that each person needs to pay.
'''
total_bill = input("What was the total bill? ")
number_of_people = input("How many people are there? ")
percentage_of_tip = input("What's the percentage that you want to tip? ")



#-------------------------------------------------------------------
# total_bill = int(input("What was the total bill? "))
# number_of_people = int(input("How many people are there? "))
# percentage_of_tip = input("What's the percentage that you want to tip? ").casefold().strip()
# operating_number = total_bill / number_of_people
#
# if percentage_of_tip == "5" or percentage_of_tip == "5.0" or percentage_of_tip == "five":
#     print("Everyone has to pay $" + str(operating_number * 0.05))
# elif percentage_of_tip == "10" or percentage_of_tip == "10.0" or percentage_of_tip == "ten":
#     print("Everyone has to pay $" + str(operating_number * 0.1))
# elif percentage_of_tip == "15" or percentage_of_tip == "15.0" or percentage_of_tip == "fifteen":
#     print("Everyone has to pay $" + str(operating_number * 0.15))
# elif percentage_of_tip == "20" or percentage_of_tip == "20.0" or percentage_of_tip == "twenty":
#     print("Everyone has to pay $" + str(operating_number * 0.2))
#     #I could've went on but I'm not learning anything new by doing that.
# else:
#     print("Incorrect input")