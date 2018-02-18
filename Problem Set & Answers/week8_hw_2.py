# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:56:07 2017

@author: Kenny
"""

class Account(object):
    def __init__(self, owner, account_number, amount):
        self.owner=owner
        self.account_number=account_number
        self.amount=amount
    def deposit(self, amount):
        self.amount+=amount
        
    def withdraw(self, amount):
        self.amount=self.amount-amount
        
    def __str__(self):
        return self.owner+', '+str(self.account_number)+', balance: '+str(self.amount)
    
a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print a1