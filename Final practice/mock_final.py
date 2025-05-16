# 1 a) O(1)

'''
What is the time complexity of inserting an item at the beginning of a Python list of length n?
'''

# a) O(1) 


# 2 

'''
Which of the following statements about sets is false?

'''

# b) You can store lists inside sets.

# 3


'''

Which sorting algorithm always has a time complexity of O(n log n)?
'''
# c) Merge Sort

# 4

'''
Which of the following errors is raised when a file is not found during file opening?
'''

# b) FileNotFoundError

# 5

'''
What is the space complexity of a recursive function that processes a list of size n by reducing its size by 1 in each call?
'''

# b) O(n)

# 6

lst = [[1, 2], [3, 4]]
lst2 = lst[:]
lst2[0][0] = 100
# print(lst)
# print(lst2)

# when you create a copy of a list, you still modify the original list


# 7

# s = {1, 2, 3}
# s.add((4, 5))
# s.add([6, 7])
# print(s)

# TypeError

# you can't put a list into a set


# 8 



# def mystery(lst):
#     return [x for x in lst if x % 2 == 0]

# print(mystery([1, 2, 3, 4, 5, 6]))


# 9

# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")

# b = B()


# 10



# class Counter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.limit:
#             val = self.current
#             self.current += 1
#             return val
#         else:
#             raise StopIteration

# c = Counter(3)
# for i in c:
#     print(i)

# for i in c:
#     print(i)


# 12

# def recursive_sum(lst):
#     if not lst:
#         return 0
#     return lst.pop() + recursive_sum(lst)

# print(recursive_sum([8, 8])) 


# 13

'''
 Write a function that takes a list of strings and returns a dictionary that maps each string to its length using dictionary comprehension.

 '''

def lenDict(lst):
    return {string: len(string) for string in lst}


# # print(lenDict(['hey', 'hello']))





# 14

import json
from abc import ABCMeta, abstractmethod

class Trackable:
    def __init__(self):
        self.log = []

    def record(self, action):
        self.log.append(action)

class Entity(object, metaclass = ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class Item(Trackable, Entity):   # fix 1
    def __init__(self, name, value):
        Trackable.__init__(self)  # fix 2
        self.name = name
        self.value = value

    def describe(self):
        return f"Item: {self.name}, Value: {self.value}"

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].value < right[j].value:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



try:   # another fix
    file = open('data.json', 'r')
except FileNotFoundError:
    print('file does not exist')

else:

    data = json.load(file)

    items = []
    for entry in data:
        name = entry.get('name')
        value = entry.get('value') # fixed

        if name is not None and value is not None:   # fixed
            item = Item(entry['name'], entry['value'])
            item.record("loaded")
            items.append(item)

    sorted_items = merge_sort(items)
    for i in sorted_items:
        print(i.describe())



# The entity doesn't have an init and Item is trying to inherit the constructor of entity 

# opening data.json with no mode 

