'''
This is a calculator.
It will give you basic +, -, ÷ and x
'''

firstNum = int(input("Input the first number here: "))
secondNum = int(input("Input the second number here: "))
operator = input("Input the operator you want here: ").casefold().strip()

if operator == "÷" or operator == "divide" or operator == "/":
    print('{} ÷ {} = '.format(firstNum, secondNum))
    print(firstNum / secondNum)
elif operator == "x" or operator == "multiply" or operator == "*":
    print('{} x {} = '.format(firstNum, secondNum))
    print(firstNum * secondNum)
elif operator == "+" or operator == "add":
    print('{} + {} = '.format(firstNum, secondNum))
    print(firstNum + secondNum)
elif operator == "-" or operator == "takeaway" or operator == "subtract":
    print('{} - {} = '.format(firstNum, secondNum))
    print(firstNum - secondNum)
else:
    print("Invalid input!")