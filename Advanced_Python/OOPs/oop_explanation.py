# POP:Total activity divided into multiple functions, and we can call those functions based on our requirements.

# OOP: Real time entities called objects,
# Class object and reference variables
# Class- It acts as a blueprint for objects
# Object: A physical existence of a class
# every object has properties and behaviour
# properties are specified by variables--attributes
# behaviour can be specified by methods

# Types of variables for class
#-------------------------------------

#1. Instance variables( object level variables)- if the value of a variable is varied from object to object,
# such type of variables are called object variables, In general we can define instance variable inside constructor by using self.
# we can assign default values to the instance variables

#2. Static variables (class level variables) - static variables are unchanged throughout the execution,
# a single copy will be created and shared among all the variables, it will be defined inside the class and outside of the constructor.
# ex: company name, School name , Bank etc

#3. Local variables(method level variables)-To meet a temporary requirements of the programmer,
# we can declare variables directly inside a method, are called local variables
# def m1(self):
#     x=10

#Types of method
#-------------------------------------
#1. Instance method : a method which is trying to access atleast one instance variables is called instance method,
# takes self as an argument

#2. class method : a method which trying to access the class variable is called class method ex- @classmethod

#3. static method : if we are not using any instance or static variable, then it is general utility method,
# we have to declare such method as static method ex. @staticmethod

""" instance + static _local variable ---> instance method
    static + local variable ---> static method
    local variable --> local method"""


# class Stu:
#     school_name="Chaitanya"
#     def __init__(self,sname,sid):
#         self.sname=sname
#         self.sid=sid
#
#     def stu_info(self):
#         print(self.sname,self.sid)
#
#     @classmethod
#     def school_info(cls,sname):
#         print(Stu.school_name)
#         print(id(cls))
#
#     @staticmethod
#     def stu_greet():
#         print("welcome to Chaitanya School:")
#
#
#
# s=Stu("Shanthu",101)
# s.stu_info()
# Stu.school_info("Chaitanya High School")
# s.stu_greet()


# Decorator- it's an annotation used for static and class methods to differentiate from different methods inside the class


#Reference Variable : can be used to refer objects. we can invoke functionality of object.
# for a single object , there may a chance of multiple references

# Constructor: is a special method to initialize the variables for the class. whenever creating an object constructor will be called.
# constructor overloading is not allowed in python PVM will consider the most recent constructor
# self: self in a python class refers to the instance of the class.it is used inside methods to access - not a keyword
# object variables and methods, constructor should take atleast one argument (atleast self)
# within a class constructor is optional, if we dont provide also default constructor will be called at the time of object creation

# __init__.py : is a file used in python packages, tells us that is python package. allow importing modules from that folder
# can contain package level initialization code

# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
#     def talk(self):
#         print("My name :",self.name)
#         print("My roll number : ",self.rollno)
#         print("My marks are : ",self.marks)
#
#
# s = Student("Shanth",100,90)
# s.talk()

# class Student:
#     def __init__(self):
#         print("default constructor with no arguments")
#
#     def __init__(self,name,rollno,marks):  # latest constructor will allways consider
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
#     def talk(self):
#         print("My name :",self.name)
#         print("My roll number : ",self.rollno)
#         print("My marks are : ",self.marks)
#
#
# s = Student("Shanth",100,90)
# s.talk()
#
# # Re-initailize the constructor at the object level
#
# class Test:
#     def __init__(self, name):
#         self.name = name
#
# t = Test(name="Shanthu")
# print(t.name)
# t.__init__("Manthu")
# print(t.name)


# class Hello:
#     print("Hello world")
#
# Hello()
# Hello()  # Hello world , The statement inside the class block is executed immediately, even without creating an object.
        # Code inside a class body executes when the class is defined, not when an object is created.

# is it possible to declare a method with same class name?-yes

# class Test:
#     def Test(self):
#         print("test")
#
# t=Test() # init will be executed
# t.Test() # method will be executed

# Inner class- A class inside a class is called inner class, without existing of outer class object there is no chance
# of existing inner class object
#  ex- car and engine, University and department, Human and head

# class Outer:
#     def __init__(self):
#         print("outer class object")
#
#     class Inner:
#         def __init__(self):
#             print("Inner class object")
#
#         def display(self):
#             print("Inner class method")
#
# # o=Outer()
# # i=o.Inner()
# # i.display()
#
# Outer().Inner().display() # this also works

# Garbage colection: del t1 : object no more available, t1=none : object is having a memory
# based on our requirements we can enable and disable garbage collection
#Destructor : __delete__()
# __delete__(self): will close the db conection/network connection
# gc module : gc.isenabled(), gc.disable(), gc.enable

# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.collect()
# gc.enable()
# print(gc.isenabled())