# test 1

def intersection(lst1, lst2):
    common_lst = []

    for element in lst1:
        if element in lst2:
            common_lst.append(element)

    return common_lst


def dictIntersection(d1, d2):
    new_dict = {}

    for key in d1:
        if key in d2:
            new_dict[key] = intersection(d1[key], d2[key])
        else:
            new_dict[key] = d1[key]

    return new_dict


import random

def readInput(n):
    result = {}

    for _ in range(n):
        key = int(input())

        if key not in result:
            result[key] = random.sample(range(1, 10), key)

    return result 



# n = int(input())
# k = int(input())

# d1 = readInput(n)
# d2 = readInput(k)

# intersecting_dict = dictIntersection(d1, d2)

# print(intersecting_dict)




# practice test 2


# phrase = 'hello world!'
# count = 0 
# for char in phrase:
#     if char == 'a':
#         count += 1

# try:
#     num = int(input('>'))
# except ValueError:
#     print('input causes value error')

# finally:
#     print(num * len(phrase))


# practice test 1

# lst = [[1, 2, 3], 
#        [4, 5, 6], 
#        [7, 8, 9]]

# for i in range(len(lst)):
#     for j in range(len(lst[0])):
#         temp = lst[i][j]

#         lst[i][j] = lst[i - 1][j] * 3

#         lst[i - 1][j] = temp 

#         if type(lst[i][j]) != str and lst[i][j] >= 10:
#             lst[i][j] = '*'


# for row in lst:
#     print(row)

    
