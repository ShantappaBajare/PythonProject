"""
Multithreading
----------------==------------------
Performing multiple tasks at same time is called multitasking

Process based multitasking:
  Each task is a separate independent process
  OS level

Thread based multitasking:
  Each task is an independent part of the same program
  A flow of execution is considered as a thread
  it is python object
  for every thread an independent job is available
  python provides an inbuilt module to perform this activity - threading(main thread,child thread)

  ex: servers

ways to create threads in python
1. creating a thread without using any class
2. creating a thread by extending thread class
3. creating a thread without extending thread class

Thread identification number
-----------------------------------
by using implicit variable: "ident"

Active count:
-------------------------------------------

how many active/in progress threads are available in the execution will get by active_count()

enumerate:
-----------------------
list out or calculate all active threads are running - enumerate()

"isAlive()"
"join()" : if we call join function main thread will wait until the child thread execution
with or without argument - join(10)- waits until 10 seconds

Daemon Threads
-------------------------------------------------
the threads which are executing in the background are called daemon threads.
main purpose of daemon threads is to provide support for non-daemon threads(main-threads),
 if it is facing any issue while execution or need of any kind of support
 ex- garbage collector

 t.isDaemon() or t.daemon
 t.daemon=True or t.setDaemon(True)

 once thread started we can't change is daemon nature-RuntimeError: cannot set daemon status of active thread


"""

# import time
# from threading import *
#
#
# t = Thread()   # No target function
# t.start()
#
# # print("list of active threads:",enumerate())
# l=enumerate()
# for i in l:
#     print(i)
# print("number of active threads:",active_count())
#
# print("Main Thread ID:", current_thread().ident)
# print("Child Thread ID:", t.ident)


# 1. creating a thread without using any class:

# from threading import *
# def display():
#     for i in range(2):
#         print("I am a child thread",current_thread().name())
#
# t=Thread(target=display)
# t.start()
#
# for i in range(2):
#     print("I am a main thread",current_thread().name())

# 2. creating a thread using class:

# from threading import *
# class MyThread(Thread):
#     def run(self):  # predefined method which overrides by thread , it is mandatory to use run method
#         for i in range(10):
#             print("I am a child thread")
#
# t = MyThread()
# t.start()
#
# for i in range(10):
#     print("I am a main thread")

# 2. creating a thread without extending class:

# from threading import *
# class Test:
#     def m1(self):
#         for i in range(10):
#             print("child thread")
#
# obj=Test()
# t=Thread(target=obj.m1)
# t.start()
#
# for i in range(10):
#     print("main thread")

# ex to show how threading reduces the execution time

# import time
# def doubles(number):
#     for number in number:
#         time.sleep(1)
#         print("dobles of number:", 2*number)
#
# def square(number):
#     for number in number:
#         time.sleep(1)
#         print("square of number:", number*number)
#
# num=[1,2,3,4,5]
# begin_time = time.time()
# doubles(num)
# square(num)
# end_time = time.time()
#
# print("Time taken:", end_time - begin_time)

# from threading import *
# import time
# def doubles(number):
#     for number in number:
#         time.sleep(1)
#         print("dobles of number:", 2*number)
#
# def square(number):
#     for number in number:
#         time.sleep(1)
#         print("square of number:", number*number)
#
# num=[1,2,3,4,5]
# begin_time = time.time()
#
# t1=Thread(target=doubles, args=(num,))
# t2=Thread(target=square, args=(num,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(current_thread().name)
# current_thread().name="Shantappa"
# print(current_thread().name)
# print(t1.name)
# t1.name="shantappa1"
# print(t1.name)
#
# end_time = time.time()
#
# print("Time taken:", end_time - begin_time)

""" Daemon Threads """

from threading import *

# mt=current_thread()
# print(mt.isDaemon()) # deprecated
# print(mt.daemon)
# mt.setDaemon(True) # deprecated
# mt.daemon=True

# def job():
#     print("child thread is daemon? :", t1.daemon)
#
# t1=Thread(target=job)
# print(t1.daemon)
# t1.daemon=True
# print(t1.daemon)
# t1.start()
#
# for i in range(1):
#     #print("main thread is daemon thread? :", current_thread().daemon)
#     print("main-execution")


def job1():
    for i in range(10):
        print("job1")
    t2 = Thread(target=job2)
    print(t2.daemon)
    t2.daemon=True
    print(t2.daemon)
    t2.start()
    t2.join()

def job2():
    print("job2")
def job3():
    print("job3\n")

t1=Thread(target=job1)
# t2=Thread(target=job2)
t3=Thread(target=job3)

print(t1.daemon)
t1.daemon=True
print(t1.daemon)
# print(t2.daemon)
print(t3.daemon)

t1.start()
# t2.start()
t3.start()
t1.join()
t3.join()

for i in range(1):
    print("print main thread")