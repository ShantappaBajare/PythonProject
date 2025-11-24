#what is a function?
# function is set of statements which will perform some task
# builtin functions and user defined functions
# funct declaration
# invoking a functions
#function does not take arguments not returns any values
#functions does not take arguments but returns some values
#function takes arguments but no return values
#function takes arguments and also returns values
# global variables can be created inside or outside the function but need to specify the global keyword when it is created inside the function

#declaration and calling--#function does not take arguments not returns any values
# def myfunc():  # with no arguments
#     print("Hello World")
# myfunc()

# def myfunc(name):   #with name argument= "Shantappa"  #function takes arguments but no return values
#     print("Hello",name)
# myfunc("Shanta")

# def cal(a,b,c):
#     return a+b+c
# print(cal(1,2,3))

# def func():  #functions does not take arguments but returns some values
#     return
# print(func())---None

# def func():
#     i=10
# print(func())--None

# def cal(a,b):  #function takes arguments and also returns values
#     print(a+b)
#
# cal(1,2)

# def cal(a,b,c):
#     return a+b+c
# print(cal(1,2,3))

# Variables
# ---------------------------------------------------------------------------------------------------------

# Global variables-The variables are created outside the function are called global variables-accessed anywhere
# Local variables-The variables are created inside the function are called local variables-accesses inside the function

# global_var= 20
#
# def func():
#     local_var=10
#     print(local_var)
#     print(global_var)
#
# func()
# print(local_var)---invalid
# print(global_var)--valid

# xy=100
#
# def cool():
#     xy=200
#     print(xy)
# cool()   #---200 but warning is shadow name from outer scope


# xy=100
# def cool():
#     global xy = 200 is invalid statement
#     global xy # first make it global declare
#     xy = 200 # then assign the new values
#     print(xy)

# cool() # if the cool function did not call the original value will be assigned to the global variable
# print(xy)

# def cool():
#     global xy
#     xy=200
#     print(xy)
# cool()
# print(xy)

# Types of arguments/parameters we can pass to the function
#------------------------------------------------------------------------------------------------------------------
#1. Positional arguments
#2. Keyword arguments

#1. Positional Arguments

# def func(i,j):
#     print(i,j)
#
# func(1,2)

#2. Keyword arguments
# def func(i,j):
#     print(i,j)
#
# func(j=2,i=1)

