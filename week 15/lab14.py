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


# print(isOccurence([2, 4, 6, 7, 2], 2))


            


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




def numLst(lst):
    if not lst:
        return []
    else:
        elements = [lst[-1]] * lst[-1]
        return elements + numLst(lst[:-1])
    
# print(numLst([8, 7, 6, 5, 2]))




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


def drawLine(tick_length, label = ''):
    line = '-' * tick_length 
    if label:
        line += str(label)

    print(line)


def drawInterval(center_length):
    if center_length > 0:
        drawInterval(center_length - 1)
        drawLine(center_length)
        drawInterval(center_length - 1)


def ruler(tick_length, inches):
    drawLine(tick_length, 0)

    for i in range(1, inches + 1):
        drawInterval(tick_length - 1)
        drawLine(tick_length, i)


# ruler(4, 4)





def listInterval(center_length):
    if center_length == 0:
        return []
    else:
        return listInterval(center_length - 1) + [center_length] + listInterval(center_length - 1)

def rulerList(inches, length):
    result = []

    for _ in range(inches):
        result.append(length)

        result.extend(listInterval(length - 1))
    
    result.append(length)

    return result


# print(rulerList(6, 6))






# def coolInterval(num):
#     if num < 1:
#         return [num]
#     else:
#         [num] + coolInterval(num - 1)
    

# print(coolInterval(5))

def coolList(num):
    interval = list(range(1, num))

    reverse = interval[::-1]

    return interval + [num] + reverse

# print(coolList(7))




def range(num):
    if num < 1:
        return []
    else:
        return range(num - 1) + [num]


def reverseRange(start, end):
    if start == end:
        return []
    else:
        return reverseRange(start + 1, end) + [start]


def coolList(num):
    start = 1
    return range(num) + reverseRange(start, num)


print(coolList(5))

