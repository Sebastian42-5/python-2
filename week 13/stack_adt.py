from __future__ import annotations
from functools import total_ordering
import time

'''
We are going to create our own abstract data structure

S.push(5) Return value -- Stack contents 5

S.push(3) Return value -- Stack content 5, 3

S.isEmpty()

S.top() Return Value 33 

|  |
|  |
----

This is how a stack looks like 

S.pop() 'Error' if it is empty 

We need to define the error 


'''
class Empty(Exception):
    '''error attempting to access an element from and empty container'''
    pass


@total_ordering
class Stack: 

    def __init__(self):
        self.__data = []

    
    def __len__(self) -> int:
        '''return length of stack'''
        return len(self.__data)
    
    def isEmpty(self) -> bool:
        return len(self.__data) == 0
    
    def push(self, elem: object) -> None:
        '''add element elem to the top of the stack
        
        >>> s = Stack()
        >>> s.push(5)
        >>> s.push(3)
        >>> s.pop()

        3

        '''
        self.__data.append(elem)
    
    def top(self):
        '''return (but do not remove) element at the top of stack'''

        if self.isEmpty():
            raise Empty('Stack is empty')

        return self.__data[-1]
    

    def pop(self):
        '''remove element at the top of stack and return its value'''

        if self.isEmpty():
            raise Empty('Stack is empty')

        return self.__data.pop()
    

    def __repr__(self) -> str:

        ESC = '\x1b'

        YELLOW = ESC + '[33m'

        BLUE = ESC + '[34m'

        RESET = ESC + '[0m'

        print()
        print()

        if not self.isEmpty():

            print(YELLOW + '|' + str(self.top()).center(9) + '|' + '\n' + '-' * 11 + RESET)
        
        else:
            print(YELLOW + '|' + ' '.center(9) + '|' + '\n' + '-' * 11)

        for i in range(len(self.__data) - 1)[::-1]:

            print(BLUE + '|' + str(self.__data[i]).center(9) + '|' + '\n' + '-' * 11 + RESET)


        return ''


    
    def __lt__(self, other_stack: Stack) -> bool:
        return isinstance(other_stack, Stack) and len(self.__data) < len(other_stack) 
    
    def __eq__(self, other_stack: Stack) -> bool:
        
        return isinstance(other_stack, Stack) and len(self.__data) == len(other_stack) 
    
    

'''
Base Exception 

System Exit, KeyboardInterrupt, Exception

Exception: (Empty), OsError, ArithmeticError, LookupError, NameError, ValueError, TypeError

OsError: FileNotFoundError, PermissionError

ArithmeticError: ZeroDivisionError

LookupError: IndexError, KeyError

'''



    
if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose = True)

    # S = Stack()
    # S.push(5)
    # S.push(3)
    # print(S)
#     print(len(S))
#     S.pop()
#     print(S)
#     print(S.isEmpty())
#     S.pop()
#     print(S)
#     print(S.isEmpty())
#     S.pop()
#     print(S)


    stack = Stack()
    time.sleep(2)

    stack.push(5)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)
    time.sleep(2)

    print(len(stack))
    stack.pop()
    print(stack)
    time.sleep(2)

    # print(stack.isEmpty())
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # print(stack)
    # time.sleep(2)

    # print(stack.isEmpty())
    # stack.pop()
    # print(stack)

    new_stack = Stack()

    new_stack.push(1)

    new_stack.push(8)

    new_stack.push(7)

    new_stack.push(9)

    print(stack < new_stack)

    print(stack == new_stack)



    






'''
ESC = '\x1b'

YELLOW = ESC + '[33m'

BLUE = ESC + '[34m'

GREEN = ESC + '[32m'

RED = ESC + '[31m'

RESET = ESC + '[0m'


'''
    






# in the main program, with no __, the user can access the data. We want it to be private

# One underscore is not advised, so it's half accessible

# with def len() is s.len and def __len__() is len(s)


