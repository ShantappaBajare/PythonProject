"""
A generator function in Python is a special function that uses yield instead of return,
and it creates a generator object that can be iterated one value at a time — without storing the entire sequence
in memory.Each time the function hits yield, it pauses, returns the value,
and on next call resumes from where it stopped.
After the last value, calling next(g) again will raise StopIteration, so we have to put the decorator calling function
inside a try and expect block to handle

syntax:
def generator_function():
    yield value

print(next(generator_function()))

Why use Generators?

✔ Memory efficient – values produced one by one
✔ Faster for large data
✔ Used for streaming, reading big files, pipelines, etc.

Normal Function	                                             Generator Function
Uses return	                                                  Uses yield
Returns a single value	                                      Returns multiple values one at a time
Function ends after return	                                  Function pauses and resumes after yield
Stores all results in memory	                              Lazy evaluation (no need to store everything)

What is yield?

yield is like a return, but it pauses the function and returns a value.
When next value is requested, function continues from where it paused

Why are generators memory efficient?

Because they generate values one at a time instead of storing everything in RAM.

Example:
Generating 1 billion numbers with a list → takes GBs.
Generator → almost 0 memory.

When would you prefer a generator?

Processing large files (reading line by line)
Streaming data
Infinite sequences
Any situation where the whole result does not fit in memory

Can a generator be reused?

No. Once exhausted, it cannot generate values again unless recreated

How can you manually get values from a generator?

g = my_gen()
next(g)
next(g)

How does yield preserve function state?

Python stores:

local variables
instruction pointer
internal frame
So the function resumes exactly where it paused.

Can generators receive values from outside?

Yes, using .send():

def gen():
    x = yield
    print(x)

g = gen()
next(g)
g.send(10)
"""

# l=[x*x for x in range(100000000000000000)]    # it will give memory error bec list will store all items
# print(type(l))
# print(l)

# g=(x*x for x in range(100)) # gen will use tuple comprehension
# print(type(g))
# print(g) # will not give any output
# print(next(g)) # will provide only the first value 0
#we have to use the looping statements
# while True:
#     print(next(g))   #this will give StopIteration

# Generate square with tuple comprehension num=10
# g=(x*x for x in range(10))
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         print("No more values in generator")
#         break

#Generator Function to Generate Squares num=5

# def square_gen(n):
#     for i in range(n):
#         yield i * i
#
# g = square_gen(5)
#
# for value in g:
#     print(value)

# Generator countdown Function Using while : countdown=5

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
# g=countdown(5)
#
# for i in g:
#     print(i)

# to send a value to gen outside function : value=10
# def gen():
#     x = yield
#     print(x)
#
# g = gen()
#
# try:
#     next(g)
#     g.send(10)
# except StopIteration:
#     print("no more values")

# To generate first 10 numbers : 1,2,3,4,5,6,7,8,9,10
# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n+=1
#
# for n in firstn(10):
#     print(n)

# To generate fibonacci series using generators n=10 - 0,1,1,2,3,5,8,13,21,34

# def fib(num):
#     a, b = 0, 1
#     n=1
#     while n <= num:
#         yield a
#         a, b = b, a+b
#         n = n+1
#
# g = fib(10)
# for i in g:
#     print(i)

# import random
# import time
#
# names = ["chinnu", "vinnu", "minnu", "bannu"]
# subjects = ["python", "ruby", "java"]
#
#
# def people_list(num):
#     results = []
#     for i in range(num):
#         person = {
#             "id": i,
#             "name": random.choice(names),
#             "subject": random.choice(subjects)
#         }
#         results.append(person)
#     return results
#
#
# t1 = time.perf_counter()
# p = people_list(10)
# t2 = time.perf_counter()
#
# print("time taken:", t2 - t1)

import random
import time

names = ["chinnu", "vinnu", "minnu", "bannu"]
subjects = ["python", "ruby", "java"]

def people_list(num):
    results = []
    for i in range(num):
        person = {
            "id": i,
            "name": random.choice(names),
            "subject": random.choice(subjects)
        }
        results.append(person)
    return results

def people_generator(num):
    for i in range(num):
        person = {
            "id": i,
            "name": random.choice(names),
            "subject": random.choice(subjects)
        }
        yield person


t1 = time.perf_counter()
p = people_generator(10)
t2 = time.perf_counter()

print("time taken:", t2 - t1)

t1 = time.perf_counter()
p1 = people_list(10)
t2 = time.perf_counter()

print("time taken:", t2 - t1)