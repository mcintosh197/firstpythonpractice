# Chained conditional
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2
print(result1, result2, result3)

# and
# or
# not
# Order of operations is not, and then or

result4 = result1 or result2 or result3
print (result4)

