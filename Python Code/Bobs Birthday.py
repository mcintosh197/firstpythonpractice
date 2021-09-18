'''
This calculator will show if you're older, younger or the same age as Bob.
'''

bobsAge = 21
yourAgeAsText = input("What is your age? ") #input always returns a string
length_of_input = len(yourAgeAsText)

if length_of_input > 0 and yourAgeAsText.isdigit():
    if yourAgeAsText == 21:
        print("You're the same age as Bob")
    elif yourAgeAsText < 21:
        print("You're younger than Bob")
    elif yourAgeAsText > 21:
        print("You're older than Bob")

else:
    print("Invalid input")