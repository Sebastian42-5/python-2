'''
Write a function called isMatched that takes one string argument, 
which is a sequence of different types of parentheses 
(e.g. (, {, [, ). Your function determines if the given parentheses expression 
is matched. If so, it returns True.
Otherwise, it returns False. 

You should use your already implemented stack object to 
implement this function

For example:
()(()){([()])} # is matched --> returns True

({[])} # is not matched --> returns False

You can only use the stack object, no other data structures. 


'''

from stack import Stack

def isMatched(exp : str) -> bool:

    stack = Stack()

    for char in exp:
        if char == '(' or char == '[' or char == '{':

            stack.push(char)
        
        if stack.isEmpty():
            return False

        elif char == ')':
            if stack.pop() != '(':
                return False
        
        elif char == ']':
            if stack.pop() != '[':
                return False
        
        elif char == '}':
            if stack.pop() != '{':
                return False
    
    return stack.isEmpty()

print(isMatched('({[])}'))

