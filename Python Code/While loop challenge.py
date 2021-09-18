'''
Ask the user, "Do you like repetition? [Y/N]"
If they enter Y, then they should be asked the question again.
This continues until they enter N, whereupon the final message is "Sorry to see you go :-("
'''

# continue_looping = True
#
# while continue_looping:
#     question = input("Do you like repetition? [Y/N]").lower().strip()
#
#     if question == "yes" or question == "y":
#         continue_looping = True
#
#     elif question == "no" or question == "n":
#         print("Thought you like repetition?")
#         continue_looping = False
#
#     else:
#         print("You need to enter a yes or no!")

'''
A class contains 5 students ["Annie", "Brian", "Clare", "Danny", "Ellen"]
Create a program that takes the class role and works out percentage attendance.
It should ask if each student is present in turn. 
E.g. 
●	Is Annie present? [y/n]
●	Is Brian present? [y/n]
When the attendance for all students has been taken, print the following message: 
The percentage attendance today is: <x> %
'''

class_list = ["Annie", "Brian", "Clare", "Danny", "Ellen", "Fred", "Gwen", "Harry", "Isabella", "John"]
class_number = 0
students_here = 0
continue_looping = True
class_length = len(class_list)
one_hundred_percent = 100

while class_number < class_length:
    user_input = input(f"Is {class_list[class_number]} here? [y/n] ").lower().strip()

    if user_input == "y" or user_input == "yes":
        students_here += 1
        class_number += 1

    elif user_input == "n" or user_input == "no":
        class_number += 1

    else:
        print("You need to input yes or no")
    continue_looping = True

percentage = (students_here / len(class_list)) * one_hundred_percent

print(f"The class percentage is {percentage}%")



