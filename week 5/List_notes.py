multiples = [i for i in range(3, 30, 3)]
cubes = [(i, i**3) for i in range(5)]

# enumerate 
indexed = [(i,values) for i, values in enumerate(multiples)]

# map and filter function 
def isOdd(x):
    return x%2 != 0

def square(x):
    return x**2
"""
filter and map and zip are just like enumerate, it creates an object in the memory and the objected can be genetated
in a list
"""

'''filter takes only functions that returns boolean !!! 
it applies the bool function to multiplles and return an object for which each element in the multiples 
return true when inputed to isOdd '''

odd_filter = filter(isOdd, multiples)

""" maps apply function isOdd to multiples"""
squared_multiples = map(isOdd, multiples) 

# in this case, you can do list(map(isOdd, multiples))

'''maps apply function square to multiples''' 
squared_multiples = map(square, multiples) 

# 2 dimentional lists

list_2d = [list(range(5)), list(range(5, 20, 3)), list(range(-4, -12, -2))]

total = 0
count = 0
for lst in list_2d:
    for item in lst:
        total += item
        count += 1


# ord and chr function
"""returns the order of any value in thee ascii code"""
position = ord('f') # returns the position of f in ascii
charater = chr(155) # retuns the character at position 155


# mutability and immutability
"""We can modify list every considering there is a pointer to it
-> list in list
-> list in tuples
-> list in dicts 
-> list in ...

the same is conversely true for tuples, we can't modify a tuple every where it is"""


# augmented assignment 
"""Normally, we can't add a list with a tuple but using augmented assignement 
we automatically cast..."""

lst = []
lst += (1, 2, 3)

# also

tup = ('me') # is not a tuple
put = ('me',) # is a tuple

# don't forget the tuple with a comma if we are talking about a tuple

print(tup, put)


# lists and pointer

"""when point to a value of a list,
if we change the value of an element in the list, since there is a pointer to it,
all the variables pointing to list will eventually get that element changed """

a = [1, 2, 3]
b  =  a
b.remove(1)
c = (a, b)
c[0].append(9) #appends to both a and b, they are pointing to the same list
print(a, b)
print()
d = [[a+a], [a] + [a], [a]+[b], ([a], [b])]

d[-1][0][0].append('test') 
print(a, b)
print()
print(d)

# you can see that when a changes explicitly variables pointing to the same list changes too. 
# therefore, in this case, both variables a and b are changed.


