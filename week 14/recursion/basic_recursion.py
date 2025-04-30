'''

Recursion tree: vertices and edges

In a tree, there is no cycles, it's connected

Further, we look into rooted trees

We hang the graph from one vertex

recSum(5)

recSum(4) + 5

recSum(3) + 4

recSum(2) + 3

recSum(1) + 2

1

'''

def iterSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    return sum 



def recSum(n):
    if n == 1:
        return 1
    else:
        return recSum(n - 1) + n  # for one run, it's constant time. I am doing it n times, so n * O(1) it's O(n). 
    
# print(recSum(5))


# A frame is anything that the function needs is pushed into the stack
# The static memory is limited, the stack can run out of memory

'''
At 1, everything gets cleared from the stack. It pops the function calls out of the memory stack.
recSum(1)
recSum(2)
recSum(3)
recSum(4)
recSum(5)

'''

def recFactorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return recFactorial(n - 1) * n 
    

# print(recFactorial(5))


def badFibonacci(n):
    # check with excpetion argument if the argument is positive
    '''
    base case:

    f0 = 0 
    f1 = 1

    fn = fn-1 + fn-2

    0 1 1 2 3 5 8 13 21 ...

    f(5)

    f(4) f(3)

    f(3) f(2) f(2) + f(1)

    f(2) + f(1) f(1) + f(0) f(1) + f(0)

    f(1) + f(0)

    '''

    if n < 0:
        return 'Enter a positive number'

    if n == 0 or n == 1:
        return n
    else:
        return badFibonacci(n - 1) + badFibonacci(n - 2)


# print(badFibonacci(-3))




def goodFibonacci(n, seen = {0:0, 1:1}):
    # preferably constant storage
    if n < 0:
        return 'Enter a positive number'
    if n not in seen:
        seen[n] = goodFibonacci(n - 1, seen) + goodFibonacci(n - 2, seen)
    
    return seen[n]


'''
6

0 1 1 2 3 5 8

{0:0, 1:1}

{0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8}


'''
    
print(goodFibonacci(2))


