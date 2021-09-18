'''
When the user inputs the axel numeber he will get a print statement
[2, 2]   You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels
[2, 4]   You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels
[2, 4, 4]   You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels
'''


try:
    user_input = input("Please input the axle number you want: ").lower().strip()
    length_user_input = len(user_input)

    if length_user_input > 0 and user_input.isdigit():
        if user_input == "[2, 2]" or user_input == "2,2" or user_input == "22":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels")
        elif user_input == "[2, 4]" or user_input == "2,4" or user_input == "24":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels")
        elif user_input == "[2, 4, 4]" or user_input == "2,4,4" or user_input == "244":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels")
except ValueError:
    print("You need to input")
else:
    print("Not the correct input")

