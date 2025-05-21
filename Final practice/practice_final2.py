# practicing map and filter 


'''
1. Given a list of tuples representing coordinate pairs:

coords = [(1, 2), (3, 4), (5, 6)]
Use map and a named function to convert each tuple into a string of the form "(x, y)".

'''

def tupleStr(coords):
    return list(map(str, coords))

coords = [[1, 2], [3, 4], [5, 6]]

new_coords = tupleStr(coords)

print(new_coords)


'''
given a nested_list = [[1, 3], [4, 6, 7], [4, 7, 9]]

return this version of the list:

[13, 467, 479]

'''


def unnest(lst):
    regular_lst = [(''.join(map(str, inner_lst))) for inner_lst in lst]

    int_lst = list(map(int, regular_lst))

    return int_lst

nested_list = [[1, 3], [4, 6, 7], [4, 7, 9]]

regular_lst = unnest(nested_list)

print(regular_lst)


def recursiveunnest(lst):
    pass



'''
2. Filter Keep Only Dictionaries with a Specific Key-Value Constraint
You are given a list of dictionaries:

people = [{'name': 'Anna', 'age': 17},
          {'name': 'Brian', 'age': 21},
          {'name': 'Cathy', 'age': 15},
          {'name': 'David', 'age': 19}]
Write a function is_adult that returns True if the person is 18 or older.
Use filter and is_adult to keep only the adults from the list.'''

def is_adult(person):
    return person['age'] >= 18
        
people = [{'name': 'Anna', 'age': 17},
          {'name': 'Brian', 'age': 21},
          {'name': 'Cathy', 'age': 15},
          {'name': 'David', 'age': 19}]

filtered_people = list(filter(is_adult, people))

print(filtered_people)

# filter applies a function to each elem in the list

'''
[[6, 8], [1, 3], [9, 11], [56, 59], [4, 6]] 
'''

def regularquickSort(lst):

    if len(lst) <= 1:
        return lst
    
    pivot = lst[-1]

    left = []

    right = []

    for i in range(len(lst) - 1):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
        
    return regularquickSort(left) + [pivot] + regularquickSort(right)


def nestedQuickSort(lst):

    left = []

    right = []

    pivot = lst[-1]

    for i in range(len(lst) - 1):
        if lst[i][-1] < pivot[0]:
            left.append(lst[i])
        else:
            right.append(lst[i])

    return left + [pivot] + right

nested_lst = [[5, 7, 2, 5, 3, 9], [3, 6, 3, 7], [8, 11, 7, 5], [78, 76, 43, 12, 1, 9], [2, 6, 8, 23]] 

new_lst = []


for lst in nested_lst:
    sorted_lst = regularquickSort(lst) 

    new_lst.append(sorted_lst)



print(nestedQuickSort(new_lst))


# I'll come back to this


'''
debugging / time complexity / space compelxity questions
'''


# 1

from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class Node(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def compute(self):
        pass

    def __lt__(self, other):
        return self.data < other.data

class ValueNode(Node):
    def compute(self):
        return self.data + 3

class IteratorNode(ValueNode):
    def __init__(self, data):
        super().__init__(data)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.data:
            self.idx += 1
            return self.compute()
        raise StopIteration

x = IteratorNode(2)
print(list(x))
print(list(x))


# 2



def weird_combo(tup, seen = None):
    if seen is None:
        seen = set()
    if not tup:
        return []
    if tup[0] in seen:
        return weird_combo(tup[1:], seen) # this creates a new space in the stack
    seen.add(tup[0]) # constant 
    return [tup[0]] + weird_combo(tup[1:], seen)

# print(weird_combo((2, 1, 2)))
# print(weird_combo((2, 2, 1)))

# can you concatenate a tuple into a list?

# In fact, it's recursively changing the tuple into a list of unique elements


# draw the recursive tree of this function

# space and time complexity 

# space is O(n) time is O(n)

# issue with the function: If you call the function more than once, the next function call might refer to the same seen set.
# This is because we are not creating a fresh set everytime. 

# Therefore, the default value for seen shoudl be None

# The default argument is mutable 

'''
Python's default arguments are evaluated only once when the function is defined, not each time the function is called. 
This means that if a mutable default argument is used and is mutated, it is mutated for all future calls to the function
 as well.

'''


'''
Immutable: int, float, bool, str, tuple 

Mutable: set, list and dict

'''


# 4


def quick_variant(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quick_variant(left) + middle + quick_variant(right)

# worse case and average case time-complexity? 

# O (nlgn) worse O(n^2) and it happens when the list is sorted already 

# space is O(n)

# in what outputs might this function not work?

# This function does not work for all cases, because if at one point, the pivot on the right is not placed at the end of the list, it will slice a non-pivot
# on the right. The pivot, therefore, will be place on the left, which makes the sorting messier. 

# print(quick_variant([5, 4, 3, 6]))


# 5


class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val) # O(1)

    def pop(self):
        return self.data.pop() # O(1)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)

# s = Stack()
# for x in range(1000): 
#     s.push(x)

# print(s)

# for x in range(1000): 
#     s.pop()


# time complexity with the bug is O(n^2) if we do push and pop 

# n searchs and * n shifts 

# with the fixed bug, it's O(n)


# 6

def fill_board(n, val):
    return [[val] * n for _ in range(n)]

b = fill_board(3, 0)
b[0][0] = 1
print(b)


# this creates a list of n references to the same list

# when you do for i in range, it will create a new list every time

# space complexity O(n^2)

# 7 

import json

def load_json_file(path):
    try:
        file = open(path, 'r')
    except json.JSONDecodeError:
        print("Could not decode JSON.")
    except FileNotFoundError:
        print("File not found.")
    else:
        data = json.load(file)
        file.close()
        return data
    

# you can't use it on a .json 
# they're not the same as a txt file 

# .load takes a file, not a string 
# .loads can take a string

'''
student_record = '{"name": "Lucy", "year": 1, "college": "Dawson"}'
parsed_record = json.loads(student_record)  # parse (translate) student record to python

'''


# some more recursion problems:

'''
Problem 1: Recursive Merge of Nested Dictionaries
Write a recursive function deep_merge(dict1, dict2) that merges two nested dictionaries. If a key exists in both and the values are dictionaries, merge them recursively. 
Otherwise, the value from dict2 overrides dict1.


dict1 = {'a': 1, 'b': {'x': 5, 'y': 6}}
dict2 = {'b': {'y': 10, 'z': 3}, 'c': 8}
Expected result:


{'a': 1, 'b': {'x': 5, 'y': 10, 'z': 3}, 'c': 8}

'''
def deepMerge(d1, d2):
    new_dict = {}

    for key in d1:
        if key in d2:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                new_dict[key] = deepMerge(d1[key], d2[key])
            else:
                new_dict[key] = d2[key]
        
        else:
            new_dict[key] = d1[key]

    
    for key in d2:
        if key not in new_dict:
            new_dict[key] = d2[key]
    
    return new_dict

dict1 = {'a': 1, 'b': {'x': 5, 'y': 6}}
dict2 = {'b': {'y': 10, 'z': 3}, 'c': 8}

print(deepMerge(dict1, dict2))

    
'''
Problem 4: Recursive RLE Decoder
Given a string encoded in run-length encoding format like "a3b2c1", write a recursive function decode_rle(encoded) that returns the decoded string: "aaabbc".

Only use recursion—no loops or list comprehensions.
'''


def rle_decoder(encoded):
    if len(encoded) <= 1:
        return ''
    else:
        elem = encoded[0]

        multiplier = int(encoded[1])

        return elem * multiplier + rle_decoder(encoded[2:])
    

encode = 'a2b3c1'

print(rle_decoder(encode))

    

'''
### Selection Sort
```python
def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        # Find minimum element in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
```

**Time Complexity: O(n²)**
- Outer loop runs n times
- Inner loop runs (n-1) + (n-2) + ... + 1 times
- Total comparisons: n(n-1)/2
- Therefore, O(n²)

### Insertion Sort
```python
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # [5, 6, 11, 12, 13]
```

**Time Complexity: O(n²)**
- Worst case: array is reverse sorted
- Each element needs to be compared with all previous elements
- Total comparisons: 1 + 2 + ... + (n-1) = n(n-1)/2
- Therefore, O(n²)
'''



'''
Problem 2: Nested List Element Removal
Write a recursive function remove_elem(nested_list, val) that removes all occurrences of a given value from a deeply nested list of arbitrary depth.


nested_list = [1, [2, [3, 1], 4], 1, [1, [1, [5]]]]
val = 1
Expected output:
[ [2, [3], 4], [ [ [5]]]]

'''

def nestedRemoval(lst, val):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            cleaned = nestedRemoval(elem, val)
            if cleaned:
                result.append(cleaned)
        elif elem != val:
            result.append(elem)
    return result
        

nested_list = [1, [2, [3, 1], 4], 1, [1, [1, [5]]]]

val = 1

print(nestedRemoval(nested_list, val))




def gcd(a, b):
    if b == 0:
        return a 
    return gcd(b, a % b)

# print(gcd(12, 15))



'''
write a recursive function that returns the number of times a number can be added by its own integers to create a new number until the number is less than 10


945
(1) 
18
(2)
9


785693
(1)
38 
(2)
11
(3)
2

37249237489234
(1)
67 
(2)
13
(3)
4

'''

def numSums(num, count = 0):
    if num < 10:
        return count
    
    else:
        string = str(num)
        sum = oneSum(string)

        return numSums(sum, count + 1)


def oneSum(string):
    if not string:
        return 0
    else:
        first_elem = string[0]
        return int(first_elem) + oneSum(string[1:])


print(numSums(37249237489234))




# space complexity of insertion sort is O(1), time complexity is O(n^2). Same for selection sort 


input_file = open('dog.txt', 'r')

my_dict = {}

my_lst = input_file.read().split()

print(my_lst)

for i in range(len(my_lst)):
    my_dict[f'Dog{i + 1}'] = my_lst[i]


print(my_dict)

