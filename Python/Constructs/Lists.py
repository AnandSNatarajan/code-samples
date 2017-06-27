#Display List methods
my_list = [1,2]
print("Printing all list methods\n")
print(dir(my_list))

#########################################################################
# Creation and access of elements                                       #
#########################################################################
# Create a new list
print("\nExample 1.1")
my_list = [1,2,3,4]
print(my_list)
del my_list

# Create a new list with heterogenous elements
print("\nExample 1.2")
my_list = [1, "chennai", "delhi"]
print(my_list)
del my_list

# Create a nested list
print("\nExample 1.3")
my_list = [1,2,[3,4]]
print(my_list)
del my_list

# Access an element in the list - index based
print("\nExample 1.4")
my_list = [1,2,3,4]
print(my_list[1])
del my_list

# Access an element in the nested list
print("\nExample 1.5")
my_list = [[1,2],[3,4]]
print(my_list[1][1])
del my_list

# Access an element in the list - negative index
# -1 prints last element in list, -2 second last and so on
# Provind a number more than the elements of the list will cause an error.
print("\nExample 1.6")
my_list = [1,2,3,4]
print(my_list[-1])
print(my_list[-4])
del my_list

# List slicing - print elements in a particular range of the list and change them
# Will not include the last index in the range specified.
print("\nExample 1.7")
my_list = [1,2,3,4]
print(my_list[2:4])
my_list[2:4] = [6,7]
print(my_list)
del my_list

# len() : Get the length of a list
print("\nExample 1.8")
my_list = [3,4,5]
print(my_list.__len__())
del my_list

# count() : Return number of occurences of a value
print("\nExample 1.9")
my_list = [2,3,2,4,2,5]
print(my_list.count(2))
del my_list

# index() : Return index at which the value exists
print("\nExample 1.10")
my_list = [1,2,3,2,4,2,5]
print(my_list.index(2))
# Print first occurence in a particular range
print(my_list.index(2,3,6))
del my_list

#########################################################################
# In place modification of list contents                                #
#########################################################################
# append() : Add an element to the end of the list
print("\nExample 2.1")
my_list = [1,0,2]
my_list.append(10)
print(my_list)
del my_list

# remove() : Remove the first occurence of a value
print("\nExample 2.2")
my_list = [3,4,5]
my_list.remove(4)
print(my_list)
del my_list

# pop() : Remove and return value at a particular index (default : last)
print("\nExample 2.3")
my_list = [3,4,5]
print(my_list.pop(1))
print(my_list)
del my_list

# insert() : Insert object at index
print("\nExample 2.4")
my_list = [3,4,5]
my_list.insert(2,7)
# 3,4,7,5
print(my_list)
del my_list

# reverse() : In place reverse of a list
print("\nExample 2.5")
my_list = [3,4,5]
my_list.reverse()
# 5,4,3
print(my_list)
del my_list

# sort() : In place sort of a list
print("\nExample 2.6")
my_list = [6,3,1,5]
my_list.sort()
print(my_list)
# Sort in reverse
my_list = [6,3,1,5]
my_list.sort(reverse=True)
print(my_list)
del my_list

#########################################################################
# Return a different list with the operation                            #
#########################################################################
# reverse() : In place reverse of a list
print("\nExample 3.1")
my_list = [3,4,5]
my_list1 = my_list.copy()
print(my_list1)
del my_list
del my_list1

# clear() : Remove all elements from a list
print("\nExample 3.2")
my_list = [3,4,5]
my_list.clear()
print(my_list)
del my_list

help(list)