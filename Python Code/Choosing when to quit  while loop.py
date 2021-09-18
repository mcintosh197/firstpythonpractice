numberList = []
continueLooping = True

while continueLooping:
    answer = input("Please enter a number to be summed up (type = when finished) : ")

    if answer == "=":
        continueLooping = False

    elif answer.isnumeric() == False:
        print("That is not a number, please try again")

    else:
        numberList.append(float(answer))

print("The total is {}".format(sum(numberList)))
