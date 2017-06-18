#########################################################################
# Creation and access of elements in set                                #
#########################################################################
# Create a new set : set is unordered and can be heterogenous, set elements
# are immutable but set by itself is mutable.
print("\nExample 1.1")
my_set = {1,2.0,'anand', 4}
print(my_set)
del my_set

# Add elements to set
print("\nExample 1.2")
my_set = {1,2.0,'anand', 4}
my_set.add((5,6))
my_set.update({6,7})
print(my_set)
del my_set

# Update elements to set, this can take an iterable like another set as argument
print("\nExample 1.3")
my_set = {1,2.0,'anand', 4}
my_set.update([5])
my_set.update({6,7})
print(my_set)
del my_set

# Remove elements from set
print("\nExample 1.4")
my_set = {1,2.0,'anand', 4}
# Discard will print error if there is no element in that name
my_set.discard(2.0)
print(my_set)
my_set.remove(4)
print(my_set)
del my_set

#########################################################################
# Set Operations                                                        #
#########################################################################

# Difference between two sets (elements in first set that are not in second)
print("\nExample 2.1")
my_set1 = {1,3,5,7}
my_set2 = {5,7,9}
print(my_set1.difference(my_set2))
# Symmetric difference between two sets is the set of elements which are in either of
# the sets but not in their intersection eg: 1, 3, 9
print(my_set1.symmetric_difference(my_set2))
# Remove all elements that are in second set DOES NOT WORK AS INTENDED
my_set1.difference_update(my_set2)
print(my_set1)

# Union of two sets
print("\nExample 2.2")
my_set1 = {1,3,5,7}
my_set2 = {5,7,9}
print(my_set1.union(my_set2))

# Intersection of two sets
print("\nExample 2.3")
my_set1 = {1,3,5,7}
my_set2 = {5,7,9}
print(my_set1.intersection(my_set2))
# Update first set with the intersection elements
my_set1.intersection_update(my_set2)
print(my_set1)

# Intersection of two sets
print("\nExample 2.4")
my_set1 = {1,3,5,7}
my_set2 = {5,7}
print(my_set1.issubset(my_set2))
print(my_set1.issuperset(my_set2))

#########################################################################
# Frozenset                                                             #
#########################################################################

#Frozenset is immutable and can be used as a key in a dictionary
my_set1 = {1,3,5,7}
my_set2 = frozenset(my_set1)
print(my_set2)

