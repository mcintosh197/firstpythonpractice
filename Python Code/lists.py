'''
Get a value from an index
'''

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

print(colours[0])
print(colours[2])
print(colours[-1])
print(colours[0:6])
print(colours[0:6:2])

'''
Check if a value is in a list
'''

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
print("Black" in colours)  # Prints True or False

'''
Append a list
'''

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
colours.append("Black")
colours.append("White")
print("Black" in colours)  # Prints True or False

'''
Extend a list
'''

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
more_colours = ["Gray", "Navy", "Pink"]
colours.extend(more_colours)
print(colours)

'''
Add lists together
'''

primary_colours = ["Red", "Blue", "Yellow"]
secondary_colours = ["Purple", "Orange", "Green"]
main_colours = primary_colours + secondary_colours
print(main_colours)

'''
Items in a list/length of a list
'''

primary_colours = ["Red", "Blue", "Yellow"]
secondary_colours = ["Purple", "Orange", "Green"]
main_colours = primary_colours + secondary_colours
print(main_colours)
print(len(main_colours))

'''
Remove from a list
'''

cars = ['citroen', 'dacia', 'ford', 'nissan', 'renault', 'volvo']
cars.remove('dacia')
print(cars)

'''
Reverse the order of a list
'''

cars = ['citroen', 'dacia', 'ford', 'nissan', 'renault', 'volvo']
cars.reverse()
print(cars)

'''
Insert an item at a particular point in the index 
'''

cars = ['citroen', 'dacia', 'ford', 'nissan', 'renault', 'volvo']
cars.insert(3,'maserati')
print(cars)

''''
Permanently sorting a list
'''

cars = [] #create an empty list
cars.append("volvo")
cars.append("ford")
cars.append("renault")
cars.append("dacia")
cars.append("citroen")
cars.append("nissan")
print(cars)
cars.sort() #permanently sort the list
print(cars)

'''
Temporarily remove sorting a list
'''
cars = [] #create an empty list
cars.append("volvo")
cars.append("ford")
cars.append("renault")
cars.append("dacia")
cars.append("citroen")
cars.append("nissan")
print(cars)
print(sorted(cars)) #temporarily sort the list
print(cars)

'''
Removing something from a list and inserting something new
Printing the list with each word on a different space
'''

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
colours.remove("Orange")
colours.insert(1, "Purple")
print(*colours, sep= "\n")
