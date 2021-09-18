'''
This shows you if you can date someone or not
With every one million you have you can lower the age you can date.
'''

while True:
    try:
        age = int(input("How old are you? "))
        her_age = int(input("How old is she? "))
        money = int(input("How much do you have in millions? "))
    except ValueError:
        print("You need to enter your age as a number")
    else:
        break

half = age / 2
age_half = int(half)
final_calculation = age_half + 7
too_old_check = her_age - age
money_calculation = final_calculation - money

if money_calculation <=17 or too_old_check >= 11 or her_age <=17:
    print("You can't date her bro!")
elif money_calculation >=18:
    print("All good bro!")
