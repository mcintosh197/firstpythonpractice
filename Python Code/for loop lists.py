'''
Printing out a list using a for loop
'''

# cars = ['citroen', 'dacia', 'ford', 'nissan', 'renault', 'volvo']
#
# message = ""
#
# for car in cars:
#    message = message + car.title() + "\n"
#
# print(message) #this only happens once, it's not part of the for loop

'''
Iterating through a loop using full stop at the end of the list 
'''

cars = ['citroen', 'dacia', 'ford', 'nissan', 'renault', 'volvo']

message = ""

for car in cars:    #loop through the cars in the list, one car at a time
   message = message + car.title()
   if car == cars[-1]:          #if the current car is the last car (volvo)
       message = message + "."  #add a full stop after the car name.
   else:
       message =  message + ", "    #add a comma after the car name.
print(message)
