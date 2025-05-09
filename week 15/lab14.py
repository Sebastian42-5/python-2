'''
1) reverse a string recursively 

2) check if a list is sorted recursively 

3) count number of occurences of a given element in a list recursively 

4) generate all subsets of a list recursively

'''

def reverse(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverse(str[:-1])
    
# print(reverse('hello'))

def isSorted(lst):
    if len(lst) == 1:
        return True
    else:
        return lst[-1] > isSorted(lst[:-1])

# print(isSorted([1, 2, 3, 4, 5]))


def occurence(lst, n):
    
    if len(lst) == 1:
        if lst[0] == n:
            return 1
        else:
            return 0
    mid = len(lst) // 2   

    return occurence(lst[:mid], n) + occurence(lst[mid:], n)


# print(occurence([2, 2, 4, 6, 7, 2], 2))
            


def occurenceNum(lst, n):
    
    if len(lst) == 1:
        if lst[0] == n:
            return 1
        else:
            return 0
    mid = len(lst) // 2   

    return occurence(lst[:mid], n) + occurence(lst[mid:], n)



def isOccurence(lst, n):
    return occurence(lst, n) == n


print(isOccurence([2, 4, 6, 7, 2], 2))


            


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


allSubsets(set(), list(my_set), 0)




def numLst(lst):
    if not lst:
        return []
    else:
        elements = [lst[-1]] * lst[-1]
        return elements + numLst(lst[:-1])
    
print(numLst([8, 7, 6, 5, 2]))




'''
create a ruler

----0
-
--
-
---
-
--
-
----1
-
--
-
---
-
--
-
----2
-
--
-
---
-
--
-
----3

'''


'''
4 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 4



3 inch ruler major tick length 4

'''


def ruler(tick, inches):
    pass

