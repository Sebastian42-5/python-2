from __future__ import annotations

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
# from abc import ABCMeta, abstractmethod

# class Trackable:
#     def __init__(self):
#         self.log = []

#     def record(self, action):
#         self.log.append(action)

# class Entity(object, metaclass = ABCMeta):
#     @abstractmethod
#     def describe(self):
#         pass

# class Item(Trackable, Entity):   # fix 1
#     def __init__(self, name, value):
#         Trackable.__init__(self)  # fix 2
#         self.name = name
#         self.value = value

#     def describe(self):
#         return f"Item: {self.name}, Value: {self.value}"

# def merge_sort(items):
#     if len(items) <= 1:
#         return items
#     mid = len(items) // 2
#     left = merge_sort(items[:mid])
#     right = merge_sort(items[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i].value < right[j].value:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result



# try:   # another fix
#     file = open('data.json', 'r')
# except FileNotFoundError:
#     print('file does not exist')

# else:

#     data = json.load(file)

#     items = []
#     for entry in data:
#         name = entry.get('name')
#         value = entry.get('value') # fixed

#         if name is not None and value is not None:   # fixed
#             item = Item(entry['name'], entry['value'])
#             item.record("loaded")
#             items.append(item)

#     sorted_items = merge_sort(items)
#     for i in sorted_items:
#         print(i.describe())



# The entity doesn't have an init and Item is trying to inherit the constructor of entity 

# opening data.json with no mode 

    
def recursive_average(lst, index = 0, total = 0):
    if not lst:
        return 0
    if index >= len(lst):
        return total // len(lst)
    
    else:
        return recursive_average(lst, index + 1, total + lst[index])
    
# print(recursive_average([4, 6, 7, 9, 12, 14]))






'''
Question 1: Data Science + Iterators + Recursion + Files
Write a class DataAnalyzer that:

Takes the name of a .txt file in its constructor. The file contains one number per line.

Implements the iterator protocol so it yields the even numbers from the file using __iter__ and __next__.

Includes a method get_average() that recursively calculates and returns the average of the numbers in the file (even and odd).

Includes a method save_results() that writes a dictionary with keys 'even_numbers' and 'average' to a JSON file called results.json. You cannot use the with keyword.

Include proper exception handling (FileNotFoundError, ZeroDivisionError, etc.).

BONUS: Add a switch() method that reverses the order of iteration.

'''


output = open('numbers.txt', 'w')

numbers = [3, 8, 10, 13, 16, 23, 89, 90]

for num in numbers:
    output.write(str(num) + '\n')

output.close()


class DataAnalyzer:
    def __init__(self, filename):
        self.filename = filename

        self._index = 0

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        try:
            file = open(self.filename, 'r')
        except FileNotFoundError:
            print('this file does not exist')

        else:
            lines = file.readlines()

            while self._index < len(lines):

                value = int(lines[self._index])

                self._index += 1

                if value % 2 == 0:
                    return value
            file.close()
            raise StopIteration
    

    def get_average(self, index = 0, total = 0):
        try:
            file = open(self.filename, 'r')
        except FileNotFoundError:
            print('this file does not exist')
            return 0

        else:
            lines = file.readlines()
            file.close()

            if not lines:
                return 0 
            
            if index >= len(lines):
                return total // len(lines)
            
            else:
                return self.get_average(index + 1, total + int(lines[index]))
        

    def save_results(self):
        try:
            js = open('analysis.json', 'w')

            our_dict = {}

            even_numbers = []

            for num in self:
                even_numbers.append(num)

            our_dict['even_numbers'] = even_numbers

            our_dict['average'] = self.get_average()

            json.dump(our_dict, js, indent = 4)

            js.close()
        except Exception as e:
            print(f'info not saved because of {e}')



# if __name__ == '__main__':
#     my_data = DataAnalyzer('numbers.txt')

#     for number in my_data:
#         print(number)

#     print(my_data.get_average())

#     my_data.save_results()
 


'''

Question 2: Object-Oriented Design + Stack ADT + Sorting
You're building a mini file system.

Implement a class File with attributes name: str and size: int. Make it printable and sortable by size using __lt__ and __repr__.

Create an abstract base class FolderLike with an abstract method get_size().

Implement a class Folder(FolderLike) that contains a list of File objects. It must implement get_size() (sum of sizes).

Create a Stack class to represent navigation through nested folders. Implement push, pop, __len__, __repr__, and is_empty methods.

Implement a method to sort the files in a folder using insertion sort, and explain its time complexity.

Design question: Explain why Folder has-a File is a "has-a" relationship and not an "is-a".

'''

from functools import total_ordering
from abc import ABC, abstractmethod


@total_ordering
class File(ABC):
    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return f'name: {self.name}' + '\n' + f'size: {self.get_size()}mb'
    
    def __lt__(self, other_file: File) -> bool:
        return self.get_size() < other_file.get_size()
    
    @abstractmethod
    def get_size(self):
        pass


class SimpleFile(File):
    def __init__(self, name, size):
        super().__init__(name)

        self._size = size

    def get_size(self):
        return self._size


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.file_list = []

    def add_file(self, file: File):
        self.file_list.append(file)
    
    def get_size(self):
        total = 0
        for file in self.file_list:
            size = file.get_size()

            total += size

        return total


if __name__ == '__main__':
    f1 = SimpleFile('song.mp4', 13)

    f2 = SimpleFile('data.txt', 45)

    print(f1)

    print(f2)

    print(f1 < f2)

    my_folder = Folder('My stuff')

    my_folder.add_file(f1)

    my_folder.add_file(f2)

    print(my_folder)





'''
Question 3: Quick Sort + Tuples + List Comprehensions + Bisect
You are given a list of tuples of the form (str, int) representing item names and their prices.


items = [('apple', 5), ('banana', 2), ('carrot', 7), ('date', 3)]
Implement a recursive quicksort function to sort items by price.

Use list comprehensions to separate:

a list of item names

a list of item prices

Explain when the worst-case time complexity occurs for your quicksort.

After sorting, use the bisect module to find the insertion point for an item with price 4.

Explain whether ('apple', [5]) is a valid element in a set and why.

'''





'''

Question 4: Classes + Iterators + Recursion + 2D Lists
You are asked to simulate a game board using a class Board.

The board is a 2D grid (list of lists) of integers.

Write a recursive method count_occurrences(self, val) to count how many times val appears.

Implement __iter__ and __next__ so that it yields elements row by row, left to right.

Define a method flatten() that returns a list comprehension that flattens the board.

Create a subclass GameBoard that inherits from Board and adds a method highlight(val) that replaces every occurrence of val with "*".
'''




'''
Question 5: Errors + JSON + Inheritance + Polymorphism + Sorting
You're building a zoo management app.

Create an abstract class Animal with an abstract method make_sound().

Subclasses Parrot and Tiger inherit from Animal and implement make_sound() uniquely.

Use @total_ordering and implement __lt__ and __eq__ to compare animals based on age.

Implement a method to save a list of animal info into a .json file using json.dump(), and handle TypeError if an object isn't serializable.

Sort a list of animals using merge sort, and explain why its complexity is always O(n log n) regardless of the input order.

'''






'''
Question 6: Data Science Libraries + Files + Recursion + Sorting + Classes + Iterators
You are analyzing sensor data collected over time and stored in a .csv file named "sensor_readings.csv" with the following structure:


timestamp,temperature,humidity
2024-01-01 00:00,22.4,45
2024-01-01 01:00,23.1,47
2024-01-01 02:00,21.7,44
...


Tasks:
File & Pandas Integration:

Use pandas to read the file and store it in a DataFrame.

Write a function that raises a FileNotFoundError if the file does not exist (without using with).

Custom Iterator:

Create a class TemperatureIterator that:

Takes a pandas.Series of temperatures.

Implements the iterator protocol.

Only yields temperatures greater than the average (use numpy.mean for the average).

Recursion:

Write a recursive function count_above_threshold(data, threshold) that counts how many temperatures exceed a given threshold from a list.

Sorting:

Manually implement a merge sort to sort the humidity readings in descending order.

Explain why merge sort is more stable and consistently faster than quick sort on large data files.

Visualization:

Use matplotlib to plot two lines on the same graph: one for temperature and one for humidity over time.

Label axes and include a legend.

Design Reasoning:

Why is it better to separate the iteration logic from the data parsing logic into separate classes/modules?

Explain how this models polymorphism and separation of concerns in software design.



'''