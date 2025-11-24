"""
What is a Decorator?

A decorator is a function that takes another function and extends its behavior without modifying its original code.

We add extra features to a function without changing the function itself.

Why use decorators?

They are used for:
Logging
Authentication
Performance measurement
Input validation
Debugging
Rate limiting
Tracking function calls

nested functions
function can return another functiom
function can be a reference
function as perameter

need to take a function as perameter
add functionality to the function
function need to return ref of another function
"""

# def decorator_function(original_function):
#     def wrapper():
#         print("Before executing function")
#         original_function()
#         print("After executing function")
#     return wrapper
#
# @decorator_function
# def display():
#     print("Inside function")
#
# display()

"""
Decorator With Parameters:
If the original function has parameters, the wrapper must accept them:
"""

# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         result = original_function(*args, **kwargs)
#         print("After function call")
#         return result
#     return wrapper
#
# @decorator_function
# def add(a, b):
#     print("Sum is:", a + b)
#
# add(10, 20)

"""Time Calculator Decorator"""

# import time
#
# def timer(func):
#     def wrapper():
#         start = time.perf_counter()
#         func()
#         end = time.perf_counter()
#         print("Time taken:", end - start)
#     return wrapper
#
# @timer
# def process():
#     for _ in range(1000000):
#         pass
#
# process()

"""Login Check Decorator"""

# def check_login(func):
#     def wrapper(user):
#         if user != "admin":
#             print("Access Denied")
#         else:
#             func(user)
#     return wrapper
#
# @check_login
# def dashboard(user):
#     print("Welcome", user)
#
# dashboard("admin")      # allowed
# dashboard("guest")      # denied

"""Decorator Inside a Class"""

# class Demo:
#     @staticmethod
#     def hello():
#         print("Hello from static method")
#
# Demo.hello()

"""Function Without @ Syntax"""
# def decorator_function(original_function):
#     def wrapper():
#         print("Before function call")
#         original_function()
#         print("After function call")
#     return wrapper
#
#
# def test():
#     print("Inside test function")
#
#
# decorated_test = decorator_function(test)
# decorated_test()


"""
| Feature       | Meaning                                             |
| ------------- | --------------------------------------------------- |
| Decorator     | Function that modifies behavior of another function |
| Uses          | Logging, security, performance, validation          |
| Applied using | `@decorator_name`                                   |
| Wrapper       | Inner function that actually adds new behavior      |

"""

"""Using @ Syntax (Simpler)"""

# def decorator_function(original_function):
#     def wrapper():
#         print("Before function call")
#         original_function()
#         print("After function call")
#     return wrapper
#
#
# @decorator_function
# def test():
#     print("Inside test function")

# test()


#function can return another functiom

# def outer():
#     x=3
#     def inner():
#         y=3
#         res= x+y
#         return res
#     return inner() # func returns x+y=6
#     # return inner # object ref of a-memory address
#
#
# a = outer()
# print(a)  # here in decorators instance of outer method a will acquire return of inner res
# print(a.__name__)

# def outer():
#     x='3'
#     def inner():
#         y='3'
#         res= x+y
#         return res
#     return inner # func returns x+y=6
#     # return inner # object ref of a-memory address
#
#
# a = outer()
# print(a.__name__) # called method name
# print(a())  # calling inner method from outside

""" its allowed to provide a function as an argument to another function"""

# def function1():
#     print("I am function1 method")
#
# def function2(func):
#     print("I am function2 method")
#     return func
#
# function2(function1)

""""""

# def string():
#     return "good morning"
#
# def string_upper(func):
#     def inner():
#         var = func()
#         var = var.upper()
#         return var
#     return inner   # if we are returning function ref then while calling we need to call function
#
# obj=string_upper(string)
# print(obj())

""" now for the above code simple and pythonic way is """

# def string_upper(func):
#     def inner():
#         var = func()
#         return var.upper()
#     return inner       # return function ref, not result
#
#
# @string_upper
# def string():
#     return "good morning"
#
# print(string())

def dev_decorator(func):
    def inner(x,y):
        if y==0:
            return "y should be >=1"
        return func(x,y)
    return inner   # inner()- it means function value then while calling just call ref

@dev_decorator
def div(a,b):
    return a/b

print(div(3,4))