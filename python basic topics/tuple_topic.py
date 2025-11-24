# a tuple is a collection which is ordered and immutable
# which is written inside () parenthesis
# we cannot append new value
# we cannot remove a value
# we cannot insert new value


# mytuple=("apple","banana","orange")
# print(mytuple)
#
# mytuple=("apple","banana","orange")
# print(mytuple[1])
# print(mytuple[-2])
# print(mytuple[-2:-1])
# print(list(mytuple))

# by default tuples does not allow to change values bec its immutable but there is a workaround
# or indirect way to change the tuples by converting the tuple into list then again converting to tuple will result

# mytuple=("apple","banana","orange")
# mylist=list(mytuple)
# mylist[1]="mango"
# mytuple=tuple(mylist)
# print(mytuple)

#copying a tuple from one to another tuple is possible
# mytuple=("apple","banana","orange")
# print(mytuple)
# mytuple2=mytuple
# print(mytuple2)
# del mytuple
# print(mytuple)

# mytuple=("apple","banana","orange")
# mytuple2=("mango",)
# mytuple3=mytuple+mytuple2
# print(mytuple3)
