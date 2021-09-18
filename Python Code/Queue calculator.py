'''
This program will tell you what line to go into based on the first letter of your surname
'''

student_surname = input("What is the first letter of your surname? ")

if student_surname <= "f":
    print("Go to queue one")
elif student_surname >="g" or student_surname <= "l":
    print("Go to queue two")