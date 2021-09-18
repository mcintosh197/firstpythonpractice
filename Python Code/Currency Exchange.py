'''
Currency exchange
This program will convert pounds to euros
'''

# while True:
#     try:
#         money_in_pounds = int(input("Enter the amount you'd like to exchange in pounds: £"))
#         exchange_rate = 1.39
#     except ValueError:
#         print("You need to enter a number!")
#     else:
#         break
#
# exchange = float(exchange_rate) * money_in_pounds
# print(f"You will get €{exchange} for £{money_in_pounds}")
# #----------------------------------------------------------------------------
# money_in_pounds = input("Enter the amount you'd like to exchange in pounds: ")
# exchange_rate = 1.39
# length_of_string = len(money_in_pounds)
#
# if length_of_string > 0 and money_in_pounds.isdigit():
#     #money_in_pounds_float = float(money_in_pounds) "Both of these ways would work to convert to a float"
#     exchange = exchange_rate * float(money_in_pounds) #This is the second way
#     print(f"You will get {exchange} euros")
# else:
#     print("You need to enter a number!")
#-----------------------------------------------------------------------------
euro_exchange_rate = 1.12
dollar_exchange_rate = 1.39

amount_to_convert = input("How much money would you like to convert? ").strip()
currency_code = input("Which currency would you like to convert EUR or USD? ").lower().strip()
length_of_string = len(amount_to_convert)

if length_of_string > 0 and amount_to_convert.isdigit():
    if currency_code == "eur":
        value_in_euro = float(amount_to_convert) * euro_exchange_rate
        print(f"£{amount_to_convert} will buy you: {value_in_euro:.2f} Euros")
    elif currency_code == "usd":
        value_in_dollars = float(amount_to_convert) * dollar_exchange_rate
        print(f"£{amount_to_convert} will buy you: {value_in_dollars:.2f} US Dollars")
else:
    print("Need to enter a number!")


