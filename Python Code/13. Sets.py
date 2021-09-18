# Unordered collection of elements
# Fast for look ups, removals and adding.
# Situation that you care it exists and doesn't exist not the order
x = set()
s = {4,32,2,2}
s2 = {3,4,22,1}
# s.add (5)
# s.remove (32)
# How to find out if something is in the list below.
print(4 in s)
# We can union these sets
print (s.union(s2))
# We can do the difference
print(s.difference(s2))
# Intersection
print (s.intersection(s2))
# Symmetric difference
print (s.symmetric_difference(s2))