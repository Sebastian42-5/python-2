'''
--> lst to work with

--> num want to insert into the lst

--> [start, end] interval of the lst to consider (defaulted to the entier lst)

>>> import bisect 

>>> lst = [1, 2, 7, 7, 7, 8, 10, 11]

>>> num = 7

>>> bisect(lst, num, start, end)

5 

returns the index where num can be inserted into lst such that lst is sorted
if num is already in the lst, returns rightmost index where num can be inserted

>>> bisect_left(lst, num, start, end)

>>> 2

returns the index where num can be inserted into lst so that lst is sorted 
if num already in lst, retruns leftmost index where num can be inserted

>>> bisect_right(lst, num, start, end)

This is the same as bisect 

'''

import bisect 

lst = [1, 2, 7, 7, 7, 8, 10, 11]

num = 7 

print(bisect.bisect(lst, num))
print(bisect.bisect_right(lst, num))
print(bisect.bisect_left(lst, num))



'''
every new sub problem
divide in two parts, split in the middle
sort the left part 
sort the right part 
merge both in a sorted order

85 24 63 45 | 17 31 96 50

85 24 | 63 45

85 | 24 

85 -> base case

24 

merged lst = [24, 85] 

63 | 45

63 

45

45 63


24 45 63 85 

'''

