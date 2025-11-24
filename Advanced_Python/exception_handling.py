""" various possible combinations of try except else finally blocks

1. try without except or finally is always invalid
2. without try block except,else and finally block is invalid
3. try and finally is valid combination
4. try and except is valid
5. try except and finally is valid
6. try except else and finally is valid
7. try except else is also valid


Types of exceptions
1. predefined exceptions
ex: zero division error, valueError

2. User defined exceptions: programmer defined
"""

"""user defined exceptions"""

class ToYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

class ToOlderException(Exception):
    def __init__(self, arg):
        self.msg = arg

age=int(input("Enter your age: "))
if age<18:
    raise ToYoungException("your age is less than 18")
elif age>=60:
    raise ToOlderException("your age is greater than 60")
else:
    print("thanks for the registration you will get the match details through mail")