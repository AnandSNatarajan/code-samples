# Dictionary is an unordered set of key:value pairs, key should be immutable

###########################################################################
# Accessing values from an existing dictionary                            #
###########################################################################

# Access an element using get
print("\nExample 1.1")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
print(my_dict['name'])
print(my_dict.get('age'))
del my_dict

# get : Access an element using get
print("\nExample 1.2")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
print(my_dict['name'])
print(my_dict.get('age'))
# Optional argument to get returns the value given if key doesnt exist
print(my_dict.get('education','b.e'))
del my_dict

# Return a new view/keys/items of dictionary elements
print("\nExample 1.3")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
print("Items")
print(my_dict.items())
print("Keys")
print(my_dict.keys())
print("Values")
print(my_dict.values())
del my_dict


###########################################################################
# Operations that modify the contents of a dictionary                     #
###########################################################################

# pop/popitem : Remove and return an element from the list
print("\nExample 2.1")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
item1 = my_dict.popitem()
print(item1)
# Return the second argument if the key doesnt exist
item1 = my_dict.pop('age2',10)
print(item1)
del my_dict

# setdefault : Add an element to the list, if they key exists overwrite it.
print("\nExample 2.2")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
my_dict.setdefault('age', 40)
my_dict.setdefault('age2', 50)
print(my_dict)
del my_dict

# update : Update the key,value paris of a particular dict with contents from another
# Add an element to the list, if they key exists overwrite it.
print("\nExample 2.3")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
my_dict2 = {'name':'Chimp', 'age2':50}
# Updates name, age2 is added
my_dict.update(my_dict2)
print(my_dict)
del my_dict

# Elegant way of creating a list
print("\nExample 2.4")
my_dict = {x : x * x for x in range (0,10)}
print(my_dict)

# del : Delete an element from the list : DOES NOT WORK
print("\nExample 2.5")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
del my_dict['name']
print(my_dict)

###########################################################################
# Operations that do not modify the contents of a dictionary              #
###########################################################################

# sorted : Returns a sorted key list.
print("\nExample 2.4")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
my_dict2 = sorted(my_dict)
print(my_dict2)
del my_dict
del my_dict2

# copy : Returns a shallow copy
print("\nExample 2.5")
my_dict = {'name':'Anand', 'age':28, 'city':'chennai'}
my_dict2 = my_dict.copy()
print(my_dict2)
del my_dict
del my_dict2


