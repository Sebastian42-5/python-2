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

if __name__ == '__main__':

    b = B() 

    b.show() 

 

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

def inPlaceQuickSort(lst):
    pass




'''
1. Data Science Libraries 
-> pandas, matplotlib, numpy 

1.5 Debugging 

Where to set a break point? 
This is the result that it's giving, this is what I want
Short answer questions


2. 2D-Lists, nested loops 

referencing, tuples
tuples are immutable objects that can have mutable objects inside


2.5 List comprehensions, map, filter 

Be sure to know how to read code that uses list comprehensions, map, filter 



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

-> basic class
-> Containment (has a)
-> inheritance (multiple) is a vs has a relationship
-> polymorphism : the method show himself differently depenidng on the class you call it on 









'''