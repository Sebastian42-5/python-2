'''
1. Data Science Libraries 
-> pandas, matplotlib, numpy 
-> mostly short answer questions 

1.5 Debugging 

Where to set a break point? 
This is the result that it's giving, this is what I want
Short answer questions


2. 2D-Lists, nested loops 

referencing, tuples
tuples are immutable objects that can have mutable objects inside


2.5 List comprehensions, map, filter 

Be sure to know how to read code that uses list comprehensions, map, filter 


2.6 Complexity 

Think about 
Inserting removing from dict set is constant 
inserting and removing from list not so much 
Think about time and space complexity. Focus on tim


3. Dictionaries, nested dictionaries, sets
sets are also immutable objects 
you can't put a mutable object inside a set 
unordered, no repetitions, you can't have a set of sets 
keys are immutable values are mutable 
string can be key, floats, tuples with no mutable objects inside, sets



4. Files (.txt and .json), Exceptions
Expected to know all the different errors (FileNotFoundError for example) how to open a file, the two different modes 
Close file. You cannot use with. 
Load, loads, dump, dumps


5. Objects / classes

-> guaranteed question!
-> pay attention to the design
-> don't forget about the type contracts
-> basic class, annotations (from __future__ import annotations) -> isinstance() taking argument of the class
-> Containment (has a)
-> inheritance (multiple) is a vs has a relationship
-> abstract classes : you can't instantiate an object of an abstract class (for example: Animal)
-> polymorphism : the method show himself differently depenidng on the class you call it on 
-> relational operators (__lt__, __eq__, etc.) + total_ordering pattern, arithmetic operators (fraction class)
-> iterators: __iter__ (returns self) __next__ (iterators vs iterable)
-> understand how to read hierarchy diagrams. Be familiar with them 

Iterators links to a for loop

beginning is going to move never comes back

and iterable is based on the iterator that lets you reset the index on what you're iterating

seq = Sequence()

for item in seq:
    print(item)

for item in seq:

it wouldn't come back to the beginning without an iterable
it creates a new sequence object behind the scenes



5.5 Stack ADT (abstract data type)

-> push 
-> pop
-> isEmpty 
-> len 
-> repr

|  |
|  |
|  |
----

Last in, first out. 
You pop from the top
You only have access to the element at the top

you can only use Stack in the final. Not the other data structures created in class


6. Recursion 

-> guaranteed question!
-> It's very important to know how recursion works. It is going to be on the final


7. Sorting and searching 

-> guaranteed question!
-> selection sort: O(n^2) and why
-> insert sort: O(n^2) and why
-> merge sort: O(nlgn) and why
-> quick sort: varies from O(nlgn) to O(n^2) (when is is O(nlgn) and when is it O(n^2)) and why 
-> binary search: O(lgn) and why 
-> remember the bisect module 



Quick sort

1. partition around pivot
2. recursion to sort on left 
3. recursion to sort right


Choosing the last element as the pivot: constant time

left [equal] right

Compare it to the pivot constant 

Put it to the left or the right

partitioning is linear time 

1. O(n)

left = n / 2
right = n / 2

the call of recursion is O(1)

equal split height is O(lgn). It's the height of the tree

The split is equal between two parts 

let's say n < n/4 3n/4

Both partitions are in terms of n, roughly speaking. 
If you have that, you can hit O(nlgn). Each split for each pivot is O(lgn) and then the partitioning n times.


let's say that a list n is sorted

we chose n to be the pivot
n 
n - 1  nothing 
n - 2  nothing
n - 3  nothing 
n - 4
... 
...
1


partitioning is O(n) the height of the tree is O(n)
so O(n^2)

if it's decreasing and you want to sort it increasing, it's the same story. 

Merge sort is consistently O(nlgn)

that is why randomized quick sort is better 


I can't say that a battery is a car, but I can say that a parrot is an animal
(is-a vs has-a relationship)


'''