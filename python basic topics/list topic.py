# A list is a collection which is ordered and changeable
# Python lists are written with square brackets
# List is mutable

# how to create a list

# mylist = [10,20,30,40]
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = []
# mylist3 = list()
#
# print(mylist)
# print(mylist1)
# print(mylist2)
# print(mylist3)

# Accessing items from the list

# mylist1 = ["apple", "banana", "cherry", "orange"]
# print(mylist1[0])
# print(mylist1[2])
# print(mylist1[1])
# print(mylist1[0:1])
# print(mylist1[-1:0])

#  range of indexes

# mylist =["apple", "banana", "cherry","mango","melon"]
# print(mylist[2:5])
# print(mylist[-4:-1])
# mylist[5]="pomo"

# append,insert,pop,del,rem function in list

# mylist = ["apple", "banana", "cherry"]
# mylist.append('orange')
# print(mylist)

# mylist=["apple","banana"]
# mylist.insert(1,"orange")
# mylist.insert(2,"pear")
# print(mylist)

# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)  #pop will removes the item with index its a method
# print(mylist)

# mylist = ["apple", "banana", "cherry"]
# del mylist[0] # del is a keyword will deletes the item with index mentioned
# print(mylist)

# mylist = ["apple", "banana", "cherry"]
# mylist.clear() # clears all items
# print(mylist)

# looping through the list
# mylist = ["apple", "banana", "cherry"]
# for x in mylist:
#     print(x)

# check if items is present in the list
# mylist = ["apple", "banana", "cherry"]
# if "apple" in mylist:
#     print("yes, apple is in the list")
# else:
#     print("No, apple is not in the list")

# length of the list
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))

# copy a list to other list
# mylist = ["apple", "banana", "cherry"]
# mylist2=list(mylist)
# print(mylist)
# print(mylist2)

# mylist = ["apple", "banana", "cherry"]
# my2=mylist.copy()
# print(mylist)
# print(my2)

# joining of lists ti 1 list
# mylist = ["apple", "banana", "cherry","pomo"]
# mylist2= ["mango", "grape", "pomo", "berry"]

# list3= mylist + mylist2 #concatinate operator
# print(list3)

#looping to combine 2 lists
# for i in mylist2:
#     mylist.append(i)
# print(mylist)

# using extend function
# mylist = ["apple", "banana", "cherry"]
# mylist2= ["mango", "grape", "pomo", "berry"]
#
# mylist.extend(mylist2)
# print(mylist)

# list comprehension- A short and powerful way to create a new list from an existing list.
#syntax:new_list = [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5] # Square of numbers
squares = [n*n for n in numbers]
print(squares) # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6] #Add condition – Even numbers only
evens = [n for n in numbers if n % 2 == 0]
print(evens) # [2, 4, 6]

names = ["john", "sara", "peter"] # Convert to Uppercase
result = [name.upper() for name in names]
print(result) # ['JOHN', 'SARA', 'PETER']

nums = [1, 2, 3] # Create a list of tuples
pairs = [(n, n*n) for n in nums]
print(pairs) # [(1, 1), (2, 4), (3, 9)]

nums = [1, 2, 3, 4, 5] #If–Else inside
result = ["even" if n % 2 == 0 else "odd" for n in nums]
print(result) #['odd', 'even', 'odd', 'even', 'odd']

result = [x*y for x in range(1, 4) for y in range(1, 4)] # nested loop
print(result) #[1, 2, 3, 2, 4, 6, 3, 6, 9]

nums = [1, 2, 3, 4] # Create dictionary using comprehension
dict_square = {n: n*n for n in nums}
print(dict_square) #{1: 1, 2: 4, 3: 9, 4: 16}

text = "Hello123World" #Filter characters from a string provides only alphabates
letters = [ch for ch in text if ch.isalpha()]
print(letters) #['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
