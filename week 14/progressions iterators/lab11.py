'''
navigator : suggest what to type and watches for mistakes

driver: types at the keyboard



You are to create a Fraction class that defines a rational number
with common arithmetic operations 

1) Define a constructor where the defualt vlaues (that is if nohting provided
by user) for the numerator and denominatir are 0 and 1 respectively

In all other cases, make sure to check for the following:

--> if denominator is 0, raise ZeroDivisionError
--> if numerator is 0, then the numerator and denominator of the object are 
0 and 1 respectively 

--> determine the sign of the fraction and put it in the numerator if it's in the denominator 
--> make sure you store in reduced form 

SWITCH ROLES OF DRIVER AND NAVIGATOR 

2) Define __add__ function that takes one argument other_fraction, adds this Fraction to other_fraction and returns the
result in reduced form. To call this function from the main program simply use the '+'
operator between the two Fraction objects

3) Define __sub__ function that takes one argument other_fraction, substracts other_fraction 
from this Fraction and returns the result in reduced form. To call this function from the main program 
simply use the '-' operator between the two fraction objects.



SWITCH ROLES OF DRIVER AND NAVIGATOR 

4) Define the __eq__ , __ne__, __gt__, __ge__, __repr__, functions. The __repr__ functions 
returns a representation of the fraction as num/denom 

SWITCH ROLES OF DRIVER AND NAVIGATOR 

5) Define the __lt__, __le__, __float__ functions functions. Note that __float__ function returns a float
representation of the fraction 

6) Create a list of Fraction objects, sort your list in descending order of given value



'''



from __future__ import annotations

from functools import total_ordering

import math

@total_ordering
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        if numerator == 0:
            self.denominator = 1
        
        if (numerator / denominator) < 0:
            self.numerator = -(abs(self.numerator))

            self.denominator = abs(self.denominator)



        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = (self.numerator // gcd)
        self.denominator = self.denominator // gcd


        # n, d = numerator, denominator

        # r = n % d

        # while r > 0:
        #     n = n // d 
        #     d = n 
        #     r = d
    

    def __repr__(self):
        return f'{self.numerator} / {self.denominator}'
    

    def __add__(self, other_fraction: Fraction) -> Fraction:
        num =  (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        denom = self.denominator * other_fraction.denominator
        return Fraction(num, denom)
    
    def __sub__(self, other_fraction: Fraction) -> Fraction:
        num =  (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        denom = self.denominator * other_fraction.denominator
        return Fraction(num, denom)
    
    def __eq__(self, other_fraction: Fraction) -> bool:
        
        return isinstance(other_fraction, Fraction) and \
            (self.numerator == other_fraction) and (self.denominator == other_fraction.denominator)
    
    def __gt__(self, other_fraction: Fraction) -> bool:
        return isinstance(other_fraction, Fraction) and \
            (self.numerator > other_fraction.numerator) and (self.denominator >= other_fraction.denominator)
            
    
    def __float__(self):
        return self.numerator / self.denominator
    

    def __truediv__(self, other_fraction: Fraction) -> Fraction:
        num = self.numerator * other_fraction.denominator
        denom = self.denominator * other_fraction.numerator

        return Fraction(num, denom)


    
        
    
 # main program
# f1 = Fraction(6,8)
# f2 = Fraction(2, 8)

# # print(f1)
# # print(f2 - f1)
# # print(f1 > f2)


# print(f1 / f2)

# print(float(f1))
# lst = []
# for i in range(1, 10):
#     lst.append(Fraction(i, i **2))


# lst.sort()
# print(lst[::-1])
