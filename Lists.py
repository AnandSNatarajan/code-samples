#Display List methods
my_list = [1,2]
print("Printing all list methods\n")
print(dir(my_list))

# Create a new list
print("\nExample 1")
my_list = [1,2,3,4]
print(my_list)
del my_list

# Create a new list with heterogenous elements
print("\nExample 2")
my_list = [1, "chennai", "delhi"]
print(my_list)
del my_list

# Create a nested list
print("\nExample 3")
my_list = [1,2,[3,4]]
print(my_list)
del my_list

# Access an element in the list - index based
print("\nExample 4")
my_list = [1,2,3,4]
print(my_list[1])
del my_list

# Access an element in the nested list
print("\nExample 5")
my_list = [[1,2],[3,4]]
print(my_list[1][1])
del my_list

# Access an element in the list - negative index
# -1 prints last element in list, -2 second last and so on
# Provind a number more than the elements of the list will cause an error.
print("\nExample 6")
my_list = [1,2,3,4]
print(my_list[-1])
print(my_list[-4])
del my_list

# List slicing - print elements in a particular range of the list and change them
# Will not include the last index in the range specified.
print("\nExample 7")
my_list = [1,2,3,4]
print(my_list[2:4])
my_list[2:4] = [6,7]
print(my_list)
del my_list

# append() : Add an element to the end of the list
print("\nExample 8")
my_list = [1,0,2]
my_list.append(10)
print(my_list)
del my_list

# len() : Get the length of a list
print("\nExample 9")
my_list = [3,4,5]
print(my_list.__len__())
del my_list

help(list)