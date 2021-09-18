# x = {"key":"value"}
x = {"key": 4}

x ["key2"] = 5
x[2] = [2,2,1,1]

print (x)

# To find something in a dictionary type
print("key" in x)
# To print all of the values (Usually want to put it in a list before)
print(list(x.values()))
# Delete something
#del x["Key"]

# Iterating through everything
for key, value in x.items ():
    print(key, value)
