x = "Kyle"

# This x=name is local so it can't be accessed outside.
# You can use global to make it not local but it's not recommended.
def func(name):
    x = name

print(x)
func("changed")
print(x)