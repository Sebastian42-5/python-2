from __future__ import annotations
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, gold):
        '''create Account with value gold'''
        self.gold = gold

    def addGold(self, amount: int) -> None:
        '''add gold amount to the account'''
        self.gold += amount 
    
    def zeroGold(self) -> None:
        self.gold = 0 

    def doubleGold(self) -> None:
        '''doubling gold amlount in account'''
        self.gold = self.gold * 2

    def __lt__(self, other: Account) -> bool:
        '''return true if account and other are of the same type 
        and gold of account is less than the gold of other'''
        return isinstance(other, Account) and \
        self.gold < other.gold 
    
    def __eq__(self, other: Account) -> bool:
        '''return true if account and other are of the same type 
        and gold of account is less than the gold of other'''
        return isinstance(other, Account) and \
        self.gold == other.gold 


# MAIN PROGRAM 

a1 = Account(500)

a2 = Account(500)

a3 = Account(56)

a4 = Account(54)


print(f'a4 < ? a3', {a4 < a3})

print(f'a1 == ? a2', {a1 == a2})

print(f'a4 > ?  a1', {a4 > a1})

print('a1 != a4 ?', {a4 != a1})
    

