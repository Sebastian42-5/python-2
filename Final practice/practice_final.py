from __future__ import annotations

# 1

def stringMergeSort(str):
    if len(str) == 1:
        return str 
    
    mid = len(str) // 2

    left = str[:mid]

    right = str[mid:]

    sorted_left = stringMergeSort(left)

    sorted_right = stringMergeSort(right)


    return merge(sorted_left, sorted_right)


def merge(left, right):
    i = 0
    j = 0

    new_str = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_str.append(left[i])
            i += 1
        else:
            new_str.append(right[j])
            j += 1

    new_str.extend(left[i:])

    new_str.extend(right[j:])

    return ''.join(new_str)


# print(stringMergeSort('hueifdgaeusifdg'))

# 2 my problem 

# 3

'''
Write an iterable that returns the next number of the factorial.
 In the constructor you should accept a start > 0 that is an integer and an
   optional end (default to 100), both inclusive. You may use `math.factorial()`
     to calculate where to begin based on "start". 

'''



# 4

 

class A: 

    def show(self): 

        print("A") 

 

class B(A): 

    def show(self): 

        print("B") 

# if __name__ == '__main__':

#     b = B() 

#     b.show() 

 

'''

5. 
Write a recursive function called sum_list that takes a list of integers as an input and returns the sum of all elements in the list.  

  

Your solution should: 

1. Use recursion 

2. Handle empty lists (return 0) 

3. Explanation of time complexity of your solution 

  

For example: 

- sum_list([1, 2, 3, 4, 5]) should return 15 

- sum_list([]) should return 0 

- sum_list([10]) should return 10 
'''

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
    

# print(sum_list([1, 2, 3, 4, 5, 6]))

# Time complexity is O(n)

# Creates n stacks to the frame, so the space complexity is O(n)



# 6 

# class Vehicle: 

#     def __init__(self,make): 

# 	    self.make = make 

#     def get_type(self): 

# 	    return 'Vehicle'



# class Car(Vehicle): 

#     def get_type(self): 
#         return 'Car'



# if __name__ == '__main__':

#     v = Vehicle("Toyota") 

#     c = Car("Honda") 

    

#     print(v.get_type()) 

#     print(c.get_type()) 



'''
is a relation: inheritance 

has a relation: using an object in another class

'''


# done in the progression class



# 8 

'''
# directory JSON:  

{  

    "\\main": {  

        "\\photos": {  

            "\\Summer Trip": {  

                "beach.png" : 2400,  

                "mountain.png" : 1200,  

                "lasagna.png" : 2000  

            },  

            "\\Winter Trip": {  

                "cabin.png" : 2000,  

                "skiing.png" : 1800  

            }  

        },  

        "\\Homework": {  

            "\\Math": {  

                "Algebra.pdf" : 1000,  

                "Statistics.txt" : 1300,  

                "\\Physics" : {  

                    "Mechanics.pdf" : 2000,  

                    "Electromagnetism.txt" : 2200  

                }  

            }  

        }  

    },  

    "\\backup": {  

        "\\photos" : {  

            "\\Summer Trip": {  

                "beach.png" : 2400,  

                "mountain.png" : 1200,  

                "city.mp4" : 5800,  

                "forest.mp4" : 5600,  

                "lasagna.png" : 2000  

            }  

        }  

    }  

}  

  

Write a recursive function to find the total size of the directory, as well as the number of each type of files in it.  

The program should export the results to a JSON file with the following structure:  

{  

    "total_size": <total_size>,  

    "file_count": {  

        "txt": <number_of_txt_files>,  

        "png": <number_of_png_files>,  

        "pdf": <number_of_pdf_files>,  

        ...  

    }  

}  

Lastly, the program should print the contents of the exported JSON file to the console.  

The program should take any arbitrary JSON representation of a directory with the sizes as input. 


'''
import json

def count_size(directory):
    return recurse(directory)

def recurse(current):

    total = 0
    counts = {}


    for name, content in current.items():
        if isinstance(content, dict):
            sub_total, sub_count = count_size(content)
            total += sub_total

            for ext, count in sub_count.items():
                counts[ext] = counts.get(ext, 0) + count
        
        else:
            total += content 
            ext = name.split('.')[-1]
            counts[ext] = counts.get(ext, 0) + 1

    
    return total, counts



def write_json(data, filename):

    output_file = open(filename, 'w')

    json.dump(data, output_file, indent = 4)


def load_json(filename):

    input_file = open(filename, 'r')

    data = json.load(input_file)

    print(data)

 
my_dir = {  

    "\\main": {  

        "\\photos": {  

            "\\Summer Trip": {  

                "beach.png" : 2400,  

                "mountain.png" : 1200,  

                "lasagna.png" : 2000  

            },  

            "\\Winter Trip": {  

                "cabin.png" : 2000,  

                "skiing.png" : 1800  

            }  

        },  

        "\\Homework": {  

            "\\Math": {  

                "Algebra.pdf" : 1000,  

                "Statistics.txt" : 1300,  

                "\\Physics" : {  

                    "Mechanics.pdf" : 2000,  

                    "Electromagnetism.txt" : 2200  

                }  

            }  

        }  

    },  

    "\\backup": {  

        "\\photos" : {  

            "\\Summer Trip": {  

                "beach.png" : 2400,  

                "mountain.png" : 1200,  

                "city.mp4" : 5800,  

                "forest.mp4" : 5600,  

                "lasagna.png" : 2000  

            }  

        }  

    }  

}  


total, count = count_size(my_dir)


result = {

    'total_size': total, 
    'total_count': count
}

filename = 'directory.json'

# write_json(result, filename)

# load_json(filename)



# 9 


'''

Task: Create a class hierarchy for a Vehicle system where: 

Vehicle is an abstract class with attributes brand and year. 

Car and Motorcycle are derived classes that inherit from Vehicle. 

Create the class such that Car can be initialized with: 

Default values (unknown, unknown, unknown) 

Brand and year only 

Year, brand, and number of seats 


'''




# 10 

'''
Do the inplace version of the quick sort 

Partitioning should be linear time

->  <- 

pointers that come in both ways 

Pick a pivot and where they stand with respect to the pointers that start 
on the extremities of the lst 

'''

def bubblePartition(lst, start, end):
    pivot_index = end
    pivot = lst[pivot_index]

    i = pivot_index - 1
    
    while i >= start:
        
        if lst[i] > pivot:
            lst[i], lst[pivot_index] = lst[pivot_index], lst[i]

            pivot_index = i
        
        else:
            j = i - 1

            while j >= start and lst[j] > lst[i]:

                lst[j], lst[i] = lst[i], lst[j]

                i = j 

                j -= 1
        
        i -= 1

    
    return pivot_index


def customQuickSort(lst, start = 0, end = None):

    if end is None:
        end = len(lst) - 1
    
    if start < end:
    
        pivot_i = bubblePartition(lst, start, end)

        customQuickSort(lst, start, pivot_i - 1)

        customQuickSort(lst, pivot_i + 1, end)


    return lst


# print(customQuickSort([5, 7, 2, 8, 1, 6, 4, 3]))





# 11




# 12

def recurPalindrome(s):
    low = 0 
    high = len(s) - 1

    if len(s) == 0:
        return False

    if low == high:
        return s[0] == s[low]
    else:
        return recurPalindrome(s[low + 1: high])
    
# the space complexity of this algorithm is O(n) 



# 13




# 20 


def mysteryFunc(n): 

    if n <= 1: 

        return n 

    return mysteryFunc(n-1) + mysteryFunc(n-2) 

# time-complexity : O(2^n)
# space complexity: O(n)



# redoing test 2 :


def readFile(file_name: str) -> dict:
    try:
        input_file = open(file_name, 'r')
    
    except FileNotFoundError:
        print('This file does not exist')
        return None
    
    else:
        d = {}
        for line in input_file:
            each_line = line.rstrip().split()

            name = each_line[0]

            data = list(map(int, each_line[1:]))

            d[name] = data 

    
    input_file.close()
    return d


# print(readFile('datas.txt'))




# object question


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class BankAccount:
    def __init__(self, person: Person, account_balance = 0):
        self.person = person
        self.account_balance = account_balance

    def __repr__(self) -> str:
        return (f'{self.person}' + '\n' + f'Balance:  {self.account_balance}')
    
    def __lt__(self, other_account: BankAccount) -> bool:
        return self.person == other_account.person and self.account_balance < other_account.account_balance
    

# if __name__ == '__main__':

#     p = Person('Sebastian', 'Soto')

#     b = BankAccount(p)

#     print(b)

#     b2 = BankAccount(p, 12)

#     print(b < b2)


# 24


def dictLst(d):
    new_lst = []

    for name, rscore in d.items():
        elem = (name, rscore)

        new_lst.append(elem)
    
    return new_lst


def rquickSort(d):

    lst = dictLst(d)

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

students = { 

    "Leo": 49.99, 

    "HHHHH": 12, 

    "bartholomew": 25, 

    "Oliver": 35.46 

} 

# print(rquickSort(students))




# 25 


'''
Find the LCP recursively

lst = ['flower', 'flow', 'flight']

returns: 'fl'

use the startswith

'''

def lcp(lst, index = 1, prefix = None):

    if not lst:
        return ''
    
    if prefix is None:
        prefix = lst[0]
    
    if index == len(lst):
        return prefix
    
    while not lst[index].startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            return ''
        
    return lcp(lst, index + 1, prefix)

# print(lcp(['flower', 'flow', 'flight']))



# 26


'''
write a recusive function that returns the flattened version of a nested lst

flatten([1, [2, [3, 4], 5], 6]) -> [1, 2. 3, 4, 5, 6]

'''

def flatten(lst, index = 0):

    if index == len(lst):
        return []
    
    elem = lst[index]

    if isinstance(elem, list):
        return flatten(elem) + flatten(lst, index + 1)
    
    else:
        return [elem] + flatten(lst, index + 1)
    

# print(flatten([1, [2, [3, 4], 5], 6]))





def sumNest(lst, index = 0):
    if index == len(lst):
        return 0
    
    elem = lst[index]

    if isinstance(elem, list):
        return sumNest(elem) + sumNest(elem, index + 1)
    
    else:
        return elem + sumNest(lst, index + 1)


# print(sumNest([1, [2, [3, 4], 5], 6]))






def sumDict(d: dict):
    if not d:
        return 0
    
    keys = list(d.keys())

    first_key = keys[0]

    first_value = d[first_key]

    remaining = {}

    i = 1

    while i < len(keys):

        k = keys[i]

        remaining[k] = d[k]

        i += 1

    if isinstance(first_value, dict):
        return sumDict(first_value) + sumDict(remaining)
    
    elif isinstance(first_value, int):

        return first_value + sumDict(remaining)
    
    else:
        return sumDict(remaining)


# print(sumDict({'a': 2, 'b':{'c': {'a': 6}}, 'd': {'e': 3}, 'f': 2}))




# 27 

'''
 Create an iterator class factorials, in which you have a method that takes an argument n and 
 returns all the factorials from 0! to n!. EXTRA: add a method called “switch” to the class that
 reverses the order of the sequence. Example: 

'''


class Factorials:
    def __init__(self, n = 0):
        self.n = n
        self._current = 0
        self.factorials = self.computeFactorials(n)

        self.reversed = False

    def computeFactorials(self, n):
        factorials = [1]

        for i in range(1, n + 1):
            factorials.append(factorials[-1] * i)
        
        return factorials
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current >= len(self.factorials):
            raise StopIteration
        else:
            if self.reversed:
                index = len(self.factorials) - 1 - self._current
            
            else:
                index = self._current

            value = self.factorials[index]

            self._current += 1

            return value
    
    def switch(self):
        self.reversed = not self.reversed
        self._current = 0
        

# if __name__ == '__main__':
#     fact = Factorials(6)

#     for elem in fact:
#         print(elem)

#     fact.switch()

#     print()

#     for elem in fact:
#         print(elem)
   


'''
Implement an iterator that filters out even values from a range iterable.

'''

# for num in EvenFIlter(range(1, 21))

class EvenFilter():
    def __init__(self, iterable):
        self.__iterable = list(iterable)

        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self._index < len(self.__iterable):
            item = self.__iterable[self._index]
            self._index += 1
            if item % 2 == 0:
                return item
        
        raise StopIteration
    

if __name__ == '__main__':
    for num in EvenFilter(range(1, 21)):
        print(num)



'''
13. Write an iterable PyramidIterable(string) that when iterated returns the 1st letter of the input string,
then the first 2, then the first 3, all the way until it returns the whole word. You will probably need to
make some sort of iterator before making your iterable. The default value for string should be 'hello world!'.
If you need to create any attributes make sure they are protected/private/public as appropriate, and justify your choice.  

Ex: PyramidIterable('cow') should return 'c', 'co', 'cow' then stop iterating.  

Ex: PyramidIterable() should return 'h', 'he', 'hel', 'hell', 'hello', 'hello ', 'hello w', ... 

'''


class PyramidIterable:
    def __init__(self, string = 'hello world!'):
        self.string = string
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self.string) + 1:
            raise StopIteration
        
        else:
            char = self.string[:self._index]

            self._index += 1

            return char 
        
if __name__ == '__main__':
    hey = PyramidIterable('cheese and ketchup')

    for elem in hey:
        print(elem)





