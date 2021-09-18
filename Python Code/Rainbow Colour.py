'''
Choosing the rainbow colour based on the colour character entered.
The input should be any of these letters (roygbiv) indicating the colours of the rainbow
'''

rainbow_colour = input("Enter the first letter of the colour you'd like the rainbow to be: ").lower().strip()

if rainbow_colour == "r":
    print("You chose red")
elif rainbow_colour == "o":
    print("You chose orange")
elif rainbow_colour == "y":
    print("You chose yellow")
elif rainbow_colour == "g":
    print("You chose green")
elif rainbow_colour == "b":
    print("You chose blue")
elif rainbow_colour == "i":
    print("You chose indigo")
elif rainbow_colour == "v":
    print("You chose violet")
else:
    print("Invalid input")