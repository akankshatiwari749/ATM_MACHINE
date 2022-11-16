#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import sys


class atm():
    def __init__(self,pin1 , balance=0):
        self.pin=pin1
        self.balance = balance

    def deposit(self, amount): # method to deposit and given amount to current balance
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount): #method to withdraw the given amount  
        self.amount = amount
        if self.amount > self.balance:# if more amount is withdraw then show  message insufficient fund
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else: #withdraw the given amount and deduct from the total balance
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def transferfunds(self, amount): #method to transfer the amount and deduct from total balance
        self.amount = amount
        checking_balance = 10000-self.amount

        self.balance = self.balance +self.amount
        print("Account balance: Nu.", self.balance)
        print()
        print("Checking Balance: Nu.", checking_balance)
        print()



    def check_balance(self): #method to check the current balance in account
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self): #method to check the transaction detail 

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 "))
            except:
                print("Error: Enter 1, 2, 3, 4 only!!!\n")
                continue
            else:
                if option == 1:
                    atm.check_balance()
                elif option == 2:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                elif option == 3:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option == 4:
                    amount = int(input("Enter the amount to transfer(Nu.):"))
                    atm.transferfunds(amount)
                else:
                    print("Wrong input")
                    sys.exit()




user={'1234':0.0}
print("*******WELCOME TO ATM*******")
print("___________________________________________________________\n")
pin1 = input("Enter the pin: ")
pin2=input("Enter the pin again: ")
if pin1 != pin2:
    print("Wrong pin. Try again.")
elif pin1 not in user:
    print("Not a registered user")
    x=input("To register enter R else N")
    if x=='R':
        data=input("Enter the pin")
        if data in user:
            print("Enter another pin")
        else:
            user[data]=0.0
    elif x=='N':
        sys.exit()
    else:
        print("Invalid input")
else:
    print("Pin verified")

atm=atm(pin1)
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("Thank you")
        break
    else:
        print("Wrong command!\n")


# In[ ]:




