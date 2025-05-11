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
