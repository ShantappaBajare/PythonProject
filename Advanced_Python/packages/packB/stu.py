class Student:
    def __init__(self,sid,sname,age):
        self.sid = sid
        self.sname = sname
        self.age = age

    def displaystu(self):
        print(self.sid,self.sname,self.age)