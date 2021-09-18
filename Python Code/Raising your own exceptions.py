'''
Raising your own exception errors.
'''

def format_name(name):
    formatted_name = name.title()  # make name title case
    formatted_name = formatted_name.replace(".", "")  # remove any . characters

    if formatted_name == "Chuck Norris":
        raise ValueError("You can't expect to use that name and live?")

    return formatted_name

while True:
    try:
        student_name = input("Enter next Student Name:  ")
        student_formatted_name = format_name(student_name)
        print(f"Welcome to Python {student_formatted_name}")
    except ValueError as kyle:
        #print("Error") #You can do this if you want something else written
        print(kyle)