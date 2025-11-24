# create a list of movies and give the info with user defined dynamic data

# class Movie:
#     def __init__(self,title,director,year,verdict):
#         self.title=title
#         self.director=director
#         self.year=year
#         self.verdict=verdict
#
#     def info(self):
#         print("title:",self.title)
#         print("director:",self.director)
#         print("year:",self.year)
#         print("verdict:",self.verdict)
#
# list_of_movies=[]
#
# while True:
#     title=input("Enter movie title: ")
#     director=input("Enter director: ")
#     year=input("Enter year: ")
#     verdict=input("Enter verdict: ")
#
#     movie=Movie(title,director,year,verdict)
#     list_of_movies.append(movie)
#
#     option=input("Would you like to add another movie? (y/n): ")
#     if option.lower()=="n":
#         break
#
# print("All movies information")
# for movie in list_of_movies:
#     movie.info()

#2. banking code to deposit and withdraw

import sys
class Customer:
    bank_name="My Bank"
    def __init__(self,name,balance = 0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance after deposit",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
            sys.exit()
        self.balance=self.balance-amount
        print("Balance after withdraw",self.balance)


print(" welcome to : ",Customer.bank_name)
name=input("Enter your name:")

c=Customer(name)

while True:
    print("d - Deposit\nw - Withdraw\nq - Quit")
    choice=input("Enter your choice:")
    if choice=="d" or choice=="D":
        amount=(int(input("Enter amount:")))
        c.deposit(amount)

    elif choice=="w" or choice=="W":
        amount=int(input("Enter amount:"))
        c.withdraw(amount)

    elif choice=="q" or choice=="Q":
        print("Thank you for banking with us")
        sys.exit()

    else:
        print("Invalid Choice")

