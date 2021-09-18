'''
Concatenating a print string
'''
firstName = "Chuck"
lastName = "Norris"

fullName = firstName + " " + lastName

print(fullName)

'''
Concatenating a print string
'''
firstName = "Chuck"
lastName = "Norris"

print(firstName,lastName)

'''
Mixing variables and strings
'''
animal1 = "fox"
animal2 = "dog"
print("The quick brown", animal1, " jumped over the lazy",animal2)

'''
mix strings, integers and floating points
'''
firstName = "Chuck"
lastName = "Norris"
age = 78
height = 1.78
print(firstName, lastName, "is", age, "years old and", height, "metres tall")
#NOTE this would have caused an error:
#print(firstname + " " + lastName + " is " + age + " years old and " + height + " metres tall"

##########################
#Example 5
##########################
animal1 = "fox"
animal2 = "dog"
print("The quick brown", animal1, "jumped over the lazy",animal2, sep='-')  #dash separator
print("The quick brown", animal1, "jumped over the lazy",animal2, sep='')  #no separator

##########################
#Example 6
##########################
animal1 = "fox"
animal2 = "dog"
print("The quick brown", animal1, "jumped over the lazy",animal2, sep=' ', end="")
print("-NOTE NO END CHAR!")
print("A new line is usually taken after every print()")
print("The quick brown", animal1, "jumped over the lazy",animal2, sep=' ',
    end=". That's all 26 letters!\n\n")
print("TA DA!")

##########################
#Example 7
##########################
firstName = "Chuck"
lastName = "Norris"
age = 78
height = 1.78
print(firstName + " " + lastName + " is " + str(age) + " years old and "
    + str(height) + " metres tall.")
print(firstName, lastName," is ", age, " years old and ", height,
    " metres tall.")

'''
f-string examples
'''
firstName = "Chuck"
lastName = "Norris"
age = 78
height = 1.78
'''
Example 1 - for this to work the variables must be in the correct order.
i.e. the first {} matches to firstName, because firstName comes first.
'''
print(f"{firstName} {lastName} is {age} years old and {height} metres tall")
