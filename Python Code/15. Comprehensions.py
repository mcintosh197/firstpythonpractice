# We can define a for loop inside of a list

x = [x for x in range (5)]
print (x)

x = [[0 for x in range(100)] for x in range(5)]
print(x)

y = [i for i in range(100) if i % 5 == 0]
print (y)