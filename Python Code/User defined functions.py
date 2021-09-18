'''
First user defined function
'''

def calculateArea(length, breadth):
    area = float(length) * float(breadth)
    return area

length = input("What is the length of the rectangle? ")
breadth = input("What is the breadth of the rectangle? ")

area_result = calculateArea(length, breadth)
print("The area of the rectangle is " + str(area_result))

'''
Another user defined function
'''

def calculate_area(length=5.0, breadth=6.0, height=5.5):
    area = float(length) * float(breadth) * float(height)
    result = "The area of the rectangle is " + str(area)
    return result

#with 2 arguments
area_result = calculate_area(3, 4)
print(area_result)

#with no arguments
area_result = calculate_area()
print(area_result)

#with the first argument only
area_result = calculate_area(3)
print(area_result)

#with the second argument only
area_result = calculate_area(breadth=4)
print(area_result)

#with the arguments in the wrong order!
area_result = calculate_area(breadth=4, length=3)
print(area_result)

