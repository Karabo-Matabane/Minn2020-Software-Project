# Given a Python list you should be able to display the Python list in descending order
aList = [100, 200, 300, 400, 500]
aList.sort(reverse=True)
print(aList)

# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
b = [i+j for i, j in zip(list1, list2)]
print(b)

# Given a Python list. Turn every item of a list into its square
bList = [1, 2, 3, 4, 5, 6, 7]
z = [i**i for i in bList]
print(z)

# Add item 7000 after 6000 in the following Python List
list3 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list3[2][2].append(7000)
print(list3)

# Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
# Only update the first occurrence of a value
list4 = [5, 10, 15, 20, 25, 50, 20]
print(20 in list4)
index = list4.index(20)
list4[index] = 200
print(list4)

# Access value from the following tuple, say 30
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][2])

# Create a tuple with single item
# note: a tuple = (10) is not a tuple
# num = (5)
# type(num) is an int type
Num = (5,)
print(type(Num))

# Unpack the following tuple into 4 variables
cTuple = (10, 20, 30, 40)
a, b, c, d = cTuple
print(a)
print(b)
print(c)
print(d)

# Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

# Counts the number of occurrences of item 50 from a tuple
tuple3 = (50, 10, 60, 70, 50)

# Two lists converted into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Merging two dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
dict3 = dict(zip(dict1, dict2))
print(dict3)

# Rename key item in a dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
for key in sampleDict:
    print(key)

# Get the key corresponding to the minimum value
sampleDict_1 = {
  'Physics': 82,
  'Math': 65,
  'history': 75}
Key_min = min(sampleDict_1, key=lambda x: sampleDict_1[x])
print(Key_min)

# Create a new dictionary by extracting: 'name' and 'salary'
sampleDict_2 = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"}

# Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

# Return a set of identical items from a given two Python set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
print(set1 & set2)

# Returns a new set with all items from both sets by removing duplicates
set_1 = {10, 20, 30, 40, 50}
set_2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
print(set1 | set2)

# Given two Python sets, update first set with items that exist only in the first set and not in the
# second set.
set3 = {10, 20, 30}
set4 = {20, 40, 50}
set3.difference_update(set4)
print(set3)

# Remove 10, 20, 30 elements from a following set at once
set_3 = {10, 20, 30, 40, 50}
set_3.difference_update({10, 20, 30})
print(set_3)

# Return a set of all elements in either A or B, but not both
set_4 = {10, 20, 30, 40, 50}
set5 = {30, 40, 50, 60, 70}
print(set_4.intersection(set5))
print(set_4 & set5)

# Remove items from set1 that are not common to both set1 and set2
set_5 = {10, 20, 30, 40, 50}
set6 = {30, 40, 50, 60, 70}
set_5.intersection_update(set6)
print(set_5)

