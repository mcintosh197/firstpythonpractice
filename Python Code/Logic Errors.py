'''
Debug this progam
'''

score = 88
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
elif score >= 40:
    grade = "E"
elif score < 40:
    grade = "F"

# if score < 40:
#     grade = "F"
# elif score >= 40:
#     grade = "E"
# elif score >= 50:
#     grade = "D"
# elif score >= 60:
#     grade = "C"
# elif score >= 70:
#     grade = "B"
# elif score >= 80:
#     grade = "A"

print("The student scored " + str(score) + " and their grade was " + grade)