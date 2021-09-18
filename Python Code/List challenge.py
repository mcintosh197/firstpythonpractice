# '''
# Finding the min, max and sum of a list
# '''
#
# numbers = list(range(20,221,5))
# print( min(numbers) )
# print( max(numbers) )
# print( sum(numbers) )


'''
List challenge
Remove something from a list
Remove something that has two in that list
Using the start, stop, step method to make different lists
Finding the last variable in the list
Sort the list into alphabetical order
Check if something is in a list
'''

olympics = ["Athens", "Paris", "St. Louis","London","Stockholm","Berlin","Antwerp","Chamonix","Paris","St. Moritz","Amsterdam","Lake Placid","Los Angeles","Garmisch-Partenkirchen","Berlin","Sapporo Garmisch-Partenkirchen","Tokyo","Helsinki","Cortina d'Ampezzo","London","St. Moritz","London","Oslo","Helsinki","Cortina d'Ampezzo","Melbourne","Stockholm","Squaw Valley","Rome","Innsbruck","Tokyo","Grenoble","Mexico City","Sapporo","Munich","Innsbruck","Montreal","Lake Placid","Moscow","Sarajevo","Los Angeles","Calgary","Seoul","Albertville","Barcelona","Lillehammer","Atlanta","Nagano","Sydney","Salt Lake City","Athens","Torino","Beijing","Vancouver","London","Sochi","Rio de Janeiro","Pyeongchang","Tokyo","Beijing","Belfast"]
# Find how many Olympics there are
olympics_length = len(olympics)
print(olympics_length)

# Removing things from the list
olympics.remove("Belfast")
olympics.remove("Berlin")

#Checking the list to see if they have removed
print(olympics)

# Creating the different types of olympics
early_olympics = olympics[:6]
print(early_olympics)
modern_olympics = olympics[6::]
print(modern_olympics)
winter_olympics = olympics[6::2]
print(winter_olympics)
summer_olympics_from_1924 = olympics[7::2]
print(summer_olympics_from_1924)

# Combine the list
summer_olympics = early_olympics + summer_olympics_from_1924
print(summer_olympics)

# Sorted the list
print(sorted(olympics))

# Checking if something is in the list
if "Belfast" in olympics:
    print("Belfast is in it")
elif "Montreal" in olympics:
    print("Montreal is in it")
