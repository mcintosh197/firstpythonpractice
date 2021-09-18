'''
This is going to print out what grade you've got.
'''

grade_percentage = int(input("Please input the grade of the student as a percentage: \n"))

if grade_percentage >= 90:
    print("You got an A")
elif grade_percentage >= 80:
    print("You got a B")
elif grade_percentage >= 70:
    print("You got a C")
elif grade_percentage >= 60:
    print("You got a D")
elif grade_percentage < 60:
    print("You got a F")
else:
    print("You need to input a number")

