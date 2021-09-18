'''
When the user inputs the number of wheels on each axle he will get a different statement.
for example: [2, 2] Will print: You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels
for example: [2, 4] Will print: You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels
For example: [2, 4, 4] Will print:  You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels
'''

while True:
    try:
        user_input = input("Please input the number of wheels on each axle: ").lower().strip()
        user_input = user_input.replace(",", "")
        user_input = user_input.replace(" ", "")
        user_input = user_input.replace("[", "")
        user_input = user_input.replace("]", "")
        user_input = user_input.replace("(", "")
        user_input = user_input.replace(")", "")
        length_of_input = len(user_input)
        if length_of_input <= 0:
            print("You need to enter the number of wheels on each axle \n For example [2,4,4]")
        elif user_input == "22" or user_input == "twotwo":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels")
        elif user_input == "24" or user_input == "twofour":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels")
        elif user_input == "244" or user_input == "twofourfour":
            print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels")
        else:
            print("You need to enter the number of wheels on each axle \n For example [2,4,4]")
    except ValueError:
        print("This is ValueError \n You need to enter the number of wheels on each axle \n For example [2,4,4]")
    except TypeError:
        print("This is a TypeError \n You need to enter the number of wheels on each axle \n For example [2,4,4]")
#
# if user_input == "22" or user_input == "twotwo":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels")
# elif user_input == "24" or user_input == "twofour":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels")
# elif user_input == "244" or user_input == "twofourfour":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels")

# user_input = input("Please input the number of wheels on each axle: ").lower().strip()
# user_input = user_input.replace(",", "")
# user_input = user_input.replace(" ", "")
# user_input = user_input.replace("[", "")
# user_input = user_input.replace("]", "")
#
# print(user_input)
#
# if user_input == "22" or user_input == "twotwo":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 2 wheels")
# elif user_input == "24" or user_input == "twofour":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels")
# elif user_input == "244" or user_input == "twofourfour":
#     print("You have 2 axles with 1st axle: 2 wheels, 2nd axle: 4 wheels, 3rd axle: 4 wheels")
# else:
#     print("Invalid input")

# while length_user_input <= 0:
#     user_input = input("Please input the number of wheels on each axle: ").lower().strip()
#     break
# if length_user_input > 0:
#     user_input = input("Please input the number of wheels on each axle: ").lower().strip()
