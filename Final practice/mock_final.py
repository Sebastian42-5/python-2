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


# if __name__ == '__main__':
#     f1 = SimpleFile('song.mp4', 13)

#     f2 = SimpleFile('data.txt', 45)

#     print(f1)

#     print(f2)

#     print(f1 < f2)

#     my_folder = Folder('My stuff')

#     my_folder.add_file(f1)

#     my_folder.add_file(f2)

#     print(my_folder)





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
import bisect

def rquickSort(lst):

    if len(lst) <= 1:
        return lst
    
    pivot = lst[-1]

    left = []

    right = []

    for i in range(len(lst) - 1):
        if lst[i][-1] < pivot[-1]:
            left.append(lst[i])
        else:
            right.append(lst[i])

    return left + [pivot] + right



items = [('apple', 5), ('banana', 2), ('carrot', 7), ('date', 3)]

sorted_lst = rquickSort(items)

# print(sorted_lst)

# names = [elem[0] for elem in sorted_lst]

# prices = [elem[-1] for elem in sorted_lst]

# print(names)

# print(prices)

# num = 4

# index_required = bisect.bisect(prices, num)

# print(index_required)



'''

Question 4: Classes + Iterators + Recursion + 2D Lists
You are asked to simulate a game board using a class Board.

The board is a 2D grid (list of lists) of integers.

Write a recursive method count_occurrences(self, val) to count how many times val appears.

Implement __iter__ and __next__ so that it yields elements row by row, left to right.

Define a method flatten() that returns a list comprehension that flattens the board.

Create a subclass GameBoard that inherits from Board and adds a method highlight(val) that replaces every occurrence of val with "*".
'''

class Board:
    def __init__(self, board):
        self.board = board

    def count_occurences(self, val, row_index = 0, col_index = 0):
        if row_index == len(self.board):
            return 0 
        
        if col_index == len(self.board[0]):
            return self.count_occurences(val, row_index + 1, 0)
        
        if self.board[col_index][row_index] == val:
            count = 1
        else:
            count = 0
        
        return count + self.count_occurences(val, row_index, col_index + 1)
    
    def flatten(self):
        return [self.board[i][j] for i in range(len(self.board[0])) for j in range(len(self.board))]



class GameBoard(Board):
    def __init__(self, board):
        super().__init__(board)

    def hightlight(self, val):
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                if self.board[i][j] == val:
                    self.board[i][j] = '*'
        
        return self.board
    
    def show(self):
        for row in self.board:
            str_line = list(map(str, row))
            line = ' '.join(str_line)

            print(line)
            

if __name__ == '__main__':
    my_board = Board([[3, 6, 3],
                      [5, 3, 6], 
                      [4, 7, 8]])
    
    print(my_board.count_occurences(3))

    print(my_board.flatten())

    
    my_game = GameBoard([[3, 6, 3],
                      [5, 3, 6], 
                      [4, 7, 8]])
    
    print(my_game.hightlight(3))

    my_game.show()



'''
Question 5: Errors + JSON + Inheritance + Polymorphism + Sorting
You're building a zoo management app.

Create an abstract class Animal with an abstract method make_sound().

Subclasses Parrot and Tiger inherit from Animal and implement make_sound() uniquely.

Use @total_ordering and implement __lt__ and __eq__ to compare animals based on age.

Implement a method to save a list of animal info into a .json file using json.dump(), and handle TypeError if an object isn't serializable.

Sort a list of animals using merge sort, and explain why its complexity is always O(n log n) regardless of the input order.

'''

class Animal(ABC):
    def __init__(self, age):
        self.age = age


    @abstractmethod
    def make_sound(self):
        pass


class Parrot(Animal):
    def __init__(self, age = 1):
        self.age = age

    def make_sound(self):
        return f'Cacaw!'

class Tiger(Animal):
    def __init__(self, age = 2):
        self.age = age
        
    def make_sound(self):
        return f'Grr!'


def animalMergeSort(animal_lst):
    pass
    




'''
Hard Problem 1: Real-Time Data Processing System
Topics Covered: Data Science Libraries, Iterators, Recursion, Sorting, Stack, Files (no with), Classes, Complexity

You are designing a real-time data processor for IoT weather sensors.

The raw sensor data comes from multiple .json files containing temperature readings and timestamps for different sensors.

Implement a class SensorReading with attributes sensor_id, timestamp, and temperature. Overload __lt__ to allow sorting by temperature.

Create a SensorStack class (based on the Stack ADT) that stores the last 10 readings for a sensor (LIFO), with proper push, pop, and __len__ methods.

Use merge sort to sort all readings across all files by temperature.

Recursively remove any readings below the mean temperature (use numpy.mean) and return the filtered list.

Make an iterator HighTempIterator that yields all readings above a dynamic threshold (set by the user during iteration).

Explain the time and space complexity of your solution.

'''

import numpy as np



@total_ordering
class SensorReading:
    def __init__(self, sensor_id, timestamp, temperature):
        self.sendor_id = sensor_id
        self.timestamp = timestamp 
        self.temperature = temperature
    
    def __lt__(self, other_reading: SensorReading):
        return other_reading.temperature < self.temperature
    
class SensorStack:
    pass

class HighTempIterator:
    pass



'''
Hard Problem 2: Custom Pandas GroupBy with OOP Integration
Topics Covered: pandas, Classes, Inheritance, Files, Iterators, JSON, Sorting, Polymorphism

You are building a mini-data analysis library to work like pandas but using custom classes.

Implement a base class Column with a method mean(). Derive NumericColumn(Column) and StringColumn(Column).

Create a class DataTable that reads a .csv file into multiple Column objects (don't use with).

Implement a custom group_by(column_name) method that returns a dictionary of groups using a nested dictionary structure.

Create a custom iterator that yields groups one by one.

Implement your own selection sort to sort numeric columns in descending order within each group.

Save each group's summary statistics (mean, max, min) to a .json file with proper exception handling.

Explain why using inheritance + polymorphism makes your design more maintainable.

'''



'''
Hard Problem 3: Recursive AST Evaluator with Visualization
Topics Covered: Recursion, Classes, Abstract Classes, Inheritance, Stack, matplotlib, JSON

Build an expression evaluator for mathematical expressions using an Abstract Syntax Tree (AST).

Define an abstract class Expression with an abstract method evaluate().

Implement Number, Add, Multiply, and Divide as subclasses.

Parse a JSON-encoded expression like:


{ "Add": [ { "Multiply": [3, 4] }, 2 ] }
into an expression tree of objects.
4. Recursively evaluate the expression.
5. Implement a Stack-based evaluator that can handle operator precedence for infix expressions.
6. Visualize the tree structure using matplotlib (nodes as circles, edges as lines).
7. Explain how recursion and the stack mirror each other in this design.

'''



'''
Hard Problem 5: Polymorphic Simulation of Sorting Algorithms
Topics Covered: Inheritance, Polymorphism, Abstract Classes, Sorting, Complexity, Data Science (numpy), Visualization

Design a framework to simulate and compare different sorting algorithms.

Create an abstract class Sorter with an abstract method sort(lst: list) -> list.

Implement MergeSorter, QuickSorter, and InsertionSorter as subclasses.

Each subclass must count and return the number of comparisons made.

Generate random data arrays using numpy.random.randint().

Plot a graph using matplotlib comparing time (x-axis) and number of comparisons (y-axis) for each algorithm over array sizes from 10 to 1000.

Save performance stats as .json with keys: algorithm name, input size, comparisons, runtime.

Explain when and why quicksort degrades to O(n^2) and how this appears on your graph.

'''




'''
Hard Problem 6: Full Simulation of an Inventory + Sales System
Topics Covered: Files, JSON, Data Science Libraries, Inheritance, Sorting, Recursion, Stack, Iterators, Tuples, List Comprehensions

You're tasked with modeling the backend of a store.

Load inventory from a .json file:

{
  "apple": {"price": 1.5, "quantity": 50},
  "banana": {"price": 1.0, "quantity": 30}
}
Create a class Product and an Inventory class to manage them.

Implement a recursive method that removes all products with quantity below a threshold.

Add a SalesStack that tracks the last 10 sales using the Stack ADT.

Allow products to be accessed via an iterator sorted by price (implement selection sort).

Use pandas to generate a daily report as a DataFrame and plot total revenue over time using matplotlib.

Include a method to save and reload state in .json, handling all exceptions.

'''