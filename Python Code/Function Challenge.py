'''
Creating a function which takes two integers and returns the largest integer.
Can't use python max function
'''

def mymax(user_input_one, user_input_two):
    if user_input_one > user_input_two:
        print(f"{user_input_one} is greater than {user_input_two}")

    elif user_input_two > user_input_one:
        print(f"{user_input_two} is greater than {user_input_one}")

def mymax3(user_input_one, user_input_two, user_input_three):
    if user_input_one > user_input_two or user_input_three:
        print(f"{user_input_one} is greater than {user_input_two} and {user_input_three}")

    elif user_input_two > user_input_one or user_input_three:
        print(f"{user_input_two} is greater than {user_input_one} and {user_input_three}")

    elif user_input_three > user_input_one or user_input_two:
        print(f"{user_input_three} is greater than {user_input_one} and {user_input_two}")

while True:
    try:
        number_of_arguments = input("Do you want to find the largest of two numbers or three? ").lower().strip()
        if number_of_arguments == "two":
            user_input_one = input("Input a number: ").strip()
            user_input_two = input("Input a second number: ").strip()
            mymax(user_input_one, user_input_two)
        elif number_of_arguments == "three":
            user_input_one = input("Input a number: ").strip()
            user_input_two = input("Input a second number: ").strip()
            user_input_three = input("Input a third number: ").strip()
            mymax3(user_input_one, user_input_two, user_input_three)
        else:
            print("You need a number! ")
        # If I want it to just do numbers then activate this code below
        # user_input_one = int(user_input_one)
        # user_input_two = int(user_input_two)
    except ValueError:
        print("You need to enter a number")
    else:
        break

# for word_value_one in user_input_one:
#     print(ord(word_value_one))
#
# for word_value_two in user_input_two:
#     print(ord(word_value_two))