#Dictionory Functions

# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

# 1. keys(): Return all keys in the dictionary
keys = my_dict.keys()
print("keys:", keys)  # dict_keys(['name', 'age', 'city'])

# 2. values(): Return all values in the dictionary
values = my_dict.values()
print("values:", values)  # dict_values(['John', 25, 'New York'])

# 3. items(): Return all key-value pairs as tuples
items = my_dict.items()
print("items:", items)  # dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

# 4. get(): Return the value for a specific key
age = my_dict.get("age")
print("get:", age)  # 25

# 5. update(): Update the dictionary with another dictionary
my_dict.update({"age": 26, "country": "USA"})
print("update:", my_dict)  # {'name': 'John', 'age': 26, 'city': 'New York', 'country': 'USA'}

# 6. pop(): Remove and return the value of a specific key
removed_value = my_dict.pop("city")
print("pop:", my_dict)  # {'name': 'John', 'age': 26, 'country': 'USA'}
print("Removed value:", removed_value)  # New York

# 7. popitem(): Remove and return the last inserted key-value pair
last_item = my_dict.popitem()
print("popitem:", my_dict)  # {'name': 'John', 'age': 26}
print("Last item:", last_item)  # ('country', 'USA')

# 8. clear(): Remove all items from the dictionary
my_dict.clear()
print("clear:", my_dict)  # {}

# List Functions

# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. append(): Add an element at the end
my_list.append(60)
print("append:", my_list)  # [10, 20, 30, 40, 50, 60]

# 2. extend(): Extend list by adding elements from another list
my_list.extend([70, 80])
print("extend:", my_list)  # [10, 20, 30, 40, 50, 60, 70, 80]

# 3. insert(): Insert an element at a specific position
my_list.insert(2, 25)
print("insert:", my_list)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# 4. remove(): Remove the first occurrence of an element
my_list.remove(30)
print("remove:", my_list)  # [10, 20, 25, 40, 50, 60, 70, 80]

# 5. pop(): Remove and return the element at a specific index
removed_element = my_list.pop(3)
print("pop:", my_list)  # [10, 20, 25, 50, 60, 70, 80]
print("Removed element:", removed_element)  # 40

# 6. index(): Return the index of the first occurrence of an element
index_of_25 = my_list.index(25)
print("index:", index_of_25)  # 2

# 7. count(): Count the occurrences of an element
count_of_20 = my_list.count(20)
print("count:", count_of_20)  # 1

# 8. sort(): Sort the list in ascending order
my_list.sort()
print("sort:", my_list)  # [10, 20, 25, 50, 60, 70, 80]

# 9. reverse(): Reverse the list
my_list.reverse()
print("reverse:", my_list)  # [80, 70, 60, 50, 25, 20, 10]

# 10. copy(): Return a shallow copy of the list
new_list = my_list.copy()
print("copy:", new_list)  # [80, 70, 60, 50, 25, 20, 10]

# 11. clear(): Remove all elements from the list
my_list.clear()
print("clear:", my_list)  # []


#Set all functions

# Creating a set
my_set = {1, 2, 3, 4, 5}

# 1. add(): Add an element to the set
my_set.add(6)
print("add:", my_set)  # {1, 2, 3, 4, 5, 6}

# 2. update(): Add multiple elements to the set
my_set.update([7, 8, 9])
print("update:", my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 3. remove(): Remove an element (raises KeyError if not found)
my_set.remove(4)
print("remove:", my_set)  # {1, 2, 3, 5, 6, 7, 8, 9}

# 4. discard(): Remove an element (does not raise error if not found)
my_set.discard(10)
print("discard:", my_set)  # {1, 2, 3, 5, 6, 7, 8, 9}

# 5. pop(): Remove and return an arbitrary element
removed_element = my_set.pop()
print("pop:", my_set)
print("Removed element:", removed_element)

# 6. clear(): Remove all elements from the set
my_set.clear()
print("clear:", my_set)  # set()

# 7. union(): Return the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("union:", union_set)  # {1, 2, 3, 4, 5}

# 8. intersection(): Return the intersection of two sets
intersection_set = set1.intersection(set2)
print("intersection:", intersection_set)  # {3}

# 9. difference(): Return the difference of two sets
difference_set = set1.difference(set2)
print("difference:", difference_set)  # {1, 2}

# 10. symmetric_difference(): Return elements in either set but not both
symmetric_diff_set = set1.symmetric_difference(set2)
print("symmetric_difference:", symmetric_diff_set)  # {1, 2, 4, 5}


#tupple Functions

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50, 20)

# 1. index(): Return the index of the first occurrence of an element
index_of_30 = my_tuple.index(30)
print("index:", index_of_30)  # 2

# 2. count(): Count the occurrences of an element
count_of_20 = my_tuple.count(20)
print("count:", count_of_20)  # 2
