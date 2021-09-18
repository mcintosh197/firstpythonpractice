'''
Print min number in the list
Print max number in the list
Print sum of the list
Print average of the list
'''

# list_of_numbers = [12, 5, 19, 15, 19, 7, 15, 2, 17, 14, 15, 18, 13, 0, 12, 8, 10, 18, 18]
#
#
# #show lowest number in the list
# print(min(list_of_numbers))
#
# #show highest number in the list
# print(max(list_of_numbers))
#
# #show the sum of the numbers in the list
#
# print(sum(list_of_numbers))
#
# #find the averge of the numbers in the list
# #average is the su of the numbers divided by how many there are
#
# average_of_numbers = sum(list_of_numbers) / len(list_of_numbers)
# print(average_of_numbers)

'''
Create a list that contains the numbers 1 to 1 million
Use min and max
Sum the numbers 
'''

# list_of_numbers = list(range(1,1000001,1))
#
# #print lowest number in the list
# print(min(list_of_numbers))
#
# #print highest number in the list
# print(max(list_of_numbers))
#
# sum_of_the_list = sum(list_of_numbers)
#
# print(f"The sum of the number 1 to 1 million is: {sum_of_the_list}")

'''
Intersect two lists together
'''

first_list = [1, 2, 3, 5, 7]
second_list = [1, 3, 5, 10, 12]
third_list = []

for item in first_list:
    if item in second_list:
        third_list.append(item)

print(third_list)

# def intersection(first_list, second_list):
#     return list(set(first_list) & set(second_list))
#
# first_list = [1, 2, 3, 5, 7]
# second_list = [1, 3, 5, 10, 12]
# print(intersection(first_list, second_list))