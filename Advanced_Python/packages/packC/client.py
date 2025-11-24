import sys
sys.path.append("/Advanced_Python/packages/packA")
sys.path.append("/Advanced_Python/packages/packB")

import emp
empobj=emp.Employee(101,"Shantappa",100000)
empobj.displayemp()

import stu
stuobj=stu.Student(100,"Shanthu",10)
stuobj.displaystu()


