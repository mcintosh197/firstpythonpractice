'''
Find errors with this program
'''
#
# numerator = input("Enter a number: ")
# denominator = input("Enter a number to divide by: ")
#
# answer = float(numerator) / float(denominator)
#
# print(answer)

'''
This is catching an error 
'''

# numerator = input("Enter a number: ")
# denominator = input("Enter a number to divide by: ")
#
# try:
#     answer = float(numerator) / float(denominator)
# except:
#     print("The numbers you entered were not valid")
# else:
#     print(answer)

'''
Catching different exceptions 
'''

# numerator = input("Enter a number: ")
# denominator = input("Enter a number to divide by: ")
#
# try:
#     answer = float(numerator) / float(denominator)
# # except ZeroDivisionError:
# #     print("ZeroDivisionError: You can't divide by zero!")
# except ZeroDivisionError:
#     print("ZeroDivisionError: You can’t divide by 0")
# except TypeError:
#     if numerator == ZeroDivisionError:
#         print(f"ZeroDivisionError: You can’t divide by 0 {numerator}")
#     elif denominator == ZeroDivisionError:
#         print(f"ZeroDivisionError: You can’t divide by 0 {denominator}")
# except ValueError:
#     print("ValueError: It's not possible to convert those values to numbers")
# else:
#     print(answer)

'''
Finally exception
'''

numerator = input("Enter a number: ")
denominator = input("Enter a number to divide by: ")

try:
    answer = float(numerator) / float(denominator)
# except ZeroDivisionError:
#     print("ZeroDivisionError: You can't divide by zero!")
except TypeError:
    print("TypeError: It's only possible to divide using numbers")
except ValueError:
    print("ValueError: It's not possible to convert those values to numbers")
else:
    print(answer)
finally:
    print("Finally: this gets done no matter what happens")

print("...and the program continues")
