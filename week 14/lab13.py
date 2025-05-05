'''
Implement a custom iterator class to generate 
even numbers in the interval [start, end]
'''
class EvenNumbers:
    def __init__(self, start = 0, end = 0):
        if start % 2 == 0:
            self._current = start
        else:
            self._current = start + 1
        self._end = end
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self._current >= self._end:
            raise StopIteration 
        else:
            even = self._current
            self._current += 2
        return even

    

if __name__ == '__main__':

    seq = EvenNumbers(1, 19)

    # for elem in seq:
        # print(elem)


'''
Implement a custom iterable class for the Fibonacci
numbers.  This class constructor should take n, 
representing the first n terms of the Fibonacci 
sequence
'''

class FibonacciIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n)


class FibonacciIterator:
    def __init__(self, n):
        self._n = n 
        
        self._count = 0

        self._first = 0
        self._second = 1
    
    def __iter__(self):
        return self

    def __next__(self):

        if self._count >= self._n:
            raise StopIteration
        
        if self._count == 0:
            result = 0
        elif self._count == 1:
            result = 1
        else:
            result = self._first + self._second

            self._first, self._second = self._second, result


        self._count += 1

        return result


# if __name__ == '__main__':
#     # for elem in FibonacciIterable(10):
#     #     print(elem)


'''
Draw the recursion tree for the computation of 
recSum(10)
'''


'''
recSum(10) 

recSum(9) + 10
recSum(8) + 9 
recSum(7) + 8 
recSum(6) + 7 
recSum(5) + 6
recSum(4) + 5
recSum(3) + 4
recSum(2) + 1
recSum(1)

'''

def recSum(n):
    if n == 1:
        print(f'recSum({n}) = {n}')
        return 1
    else:
        print(f'recSum({n - 1}) + {n}')
        return recSum(n - 1) + n
    
# print(recSum(10))


'''
write a recursive function that determines the
minimum element in a given list of integers. 
'''

def minNum(lst):
    if len(lst) == 1:
        return lst[0]
    
    sub = minNum(lst[1:])

    if lst[0] < sub:
        return lst[0]
    else:
        return sub

# print(minNum([4, 7, 8, 2, 3, 5]))

    

'''
write a recursive function that converts a string of integers
into its integer counterpart
'''

def strInt(str):

    if len(str) == 1:
        return int(str)
    else:
        return strInt(str[:-1]) * 10 + int(str[-1])
    
# print(strInt('1234'))



'''
write a recursive function to determine if a given string
is a palindrome
'''

def recurPalindrome(s):
    low = 0 
    high = len(s) - 1

    if len(s) == 0:
        return False

    if low == high:
        return s[0] == s[low]
    else:
        return recurPalindrome(s[low + 1: high])
    

# print(recurPalindrome('bananabo'))


'''
Write a recursive function to count number of vowels in a string
'''

def vowels(s):

    all_vowels = 'aeiouy'

    if len(s) == 0:
        return 0 
    else:
        first = s[0]
        if first in all_vowels:
            first = 1
        else:
            first = 0

    return first + vowels(s[1:])


'''
use recursion to determine if a string has more vowels than consonants. 
'''

def vowelsConsonants(s):
    all_vowels = 'aeiouy'

    if len(s) == 0:
        return 0 
    else:
        first = s[0]
        if first in all_vowels:
            first = 2
        else:
            first = 1

    return (first + vowels(s[1:])) % 2


result = vowels('heyyo')

if result == 1:
    print('False')
elif result == 0:
    print('True')



'''
Implement an iterator that filters out even values from a range iterable.

'''

# for num in EvenFIlter(range(1, 21))

class EvenFilter():
    def __init__(self, iterable):
        self.__iterable = iterable

        # self._start = list(iterable)[0]

        # self._end = list(iterable)[0]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        for item in self.__iterable:
            if item % 2 == 0:
                return item 
        
        raise StopIteration
    

# if __name__ == '__main__':
    # for num in EvenFilter(range(1, 21)):
        # print(num)


'''
write a recursive function that prints all subsets of a given set of elements

'''

def allSubsets(current, remaining, index):
    
    if index == len(remaining):
        print(current)
        return 
    
    elem = remaining[index]

    new_set_with_elem = current.copy() 

    new_set_with_elem.add(elem)

    allSubsets(new_set_with_elem, remaining, index + 1)

    allSubsets(current, remaining, index + 1)


my_set = {1, 2, 3}


# allSubsets(set(), list(my_set), 0)


'''
[1, 2, 3]

{1} {}

{1, 2} {2}

{1, 3} {3}

{1, 2, 3} {2, 3}

'''

def count_pairs(lst, target):

    if len(lst) < 2:
        return 0
    
    first = lst[0]

    rest = lst[1:]

    count = rest.count(target - first)

    return count + count_pairs(rest, target)

lst = [0, 1, 2, 3, 4, 6, 7, 5]

print(count_pairs(lst, 7))


'''

def goodFibonacci(n, seen = {0:0, 1:1}):
    # preferably constant storage
    if n < 0:
        return 'Enter a positive number'
    if n not in seen:
        seen[n] = goodFibonacci(n - 1, seen) + goodFibonacci(n - 2, seen)
    
    return seen[n]

'''


