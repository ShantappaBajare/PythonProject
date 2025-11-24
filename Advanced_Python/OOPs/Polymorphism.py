"""
Polymorphism : one name multiple forms. same method with multiple behaviors
Duck typing philosophy of python
Overloading
1.    Operator overloading:
operator overloading by magic methods :__add__(self,other)
whenever we are calling + operator then __add__() method will be called
whenever we are printing book object reference then __str__() method will be called

    method overloading
    constructor overloading
Overriding
    Method overiding
    constructor overriding
"""

# overloading:
# Operator overloading : Operator overloading is a feature in Python that allows the same operator (like +, -, *, ==, etc.)
# to perform different operations depending on the operands.

# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __add__(self,other):   # magic method
#         return self.pages+other.pages
#
# b1 = Book(5)
# b2 = Book(6)
# print(b1+b2)

# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __add__(self,other):   # magic method
#         total=self.pages+other.pages
#         b=Book(total)
#         return b
#
#     def __mul__(self,other):
#         total=self.pages*other.pages
#         b=Book(total)
#         return b
#
# b1 = Book(5)
# b2 = Book(6)
# b3 = Book(7)
# b4 = Book(8)
# print(b1)
# print(b2)
# print(b3)
# print(b4)
# print(b1+b2)
# print(b1+b2+b3)
# print(b1+b2+b3+b4)
# print(b1+b2*b3+b4)


#Method overloading : Method overloading is having multiple methods with the same name in a class but different parameters.
# Python does not support true method overloading, but we can achieve similar behavior using default arguments or *args.
