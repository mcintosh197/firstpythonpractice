#x = lambda x, y: x + y

#print(x(2, 32))

# How you can add two to each number in the list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mp = map(lambda i: i + 2, x)
print(list(mp))

# We can do the opposite of map 
mp= filter(lambda i: i * 2, x)
print(list(mp))
