'''
Quetion 1: Create Pascal's Triangle more efficiently than O(n^3)-time and
O(n^2) space.  


'''
# this one is done

'''
Question 2: ToyBoxes
'''

def readBoxes(n):
    lst_boxes = []

    for i in range(n):
        box = input(': ').split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        lst_boxes.append(box)

    return lst_boxes



def allBoxesOK(lst_boxes):
    for box in lst_boxes:
        if box != sorted(box):
            return False
    return True 



def boxIntervals(lst_boxes):
    intervals = []

    for box in lst_boxes:
        intervals.append([box[0], box[-1]])

    return intervals


def allIntervalsOK(lst_intervals):

    prev_max_height = lst_intervals[0][1]

    for box in range(1, len(lst_intervals)):
        current_min_height = lst_intervals[box][0]
        
        if current_min_height < prev_max_height:
            return False
        else:
            prev_max_height = lst_intervals[box][1]

    return True


# # TODO : read input 


# n = int(input('Number of boxes: '))

# boxes = readBoxes(n)


# # TODO : check if all the boxes are okay 

# if not allBoxesOK(boxes):
#     print('NO!')

# else:
#     # TODO : Obtain a new list of boxes with only the left and right heights (intervals)

#     intervals = boxIntervals(boxes)

#     # TODO : sort the boxes (the intervals)

#     intervals.sort()

#     print(intervals)

#     # TODO : determine whether the boxes are organized or not 

#     if allIntervalsOK(intervals):
#         print('YES!')

#     else:
#         print('NO!')

# This one is done (go to toyBoxes)

'''
Question 3: Baker Bonus
problem statement already online

QUESTION 2: BAKER'S BONUS

A bakery has multiple franchises opened and wants to congratulate the franchises that have performed well throughout the years, as well as congratulate everyone for performing well on certain days of the year.  

Congratulations are offered as follows:
--> if in a single day all franchises combined sell an amount of baked goods that is equivalent to multiple of baker's dozen (i.e. 13), then all franchises will receive a bonus
--> if an individual franchise, throughout its entire existence, has sold an amount of baked goods that is equivalent to a multiple of a baker's dozen (i.e. 13), then the franchise will receive a bonus.  

INPUT SPECIFICATION:
--> first line of input contains 2 values: F and D separated by a space.  F represents the number of franchises that the bakery has and D represents the number of days of information
--> on the next D lines, there will be F integers separated by spaces, such that the i-th integer online j represents the number of baked goods sold by franchise i on day j.  

OUTPUT SPECIFICATION:
Determine, for each day (across all franchises) and for each franchise (across all days), whether or not the number of baked goods sold is a multiple of 13.  If so, track how many baker's dozens were sold.  Report the total number of baker's dozens as a single integer on its own line.  



Sample Input-1
4 5
4 3 2 4
3 3 2 1
8 2 4 1
2 2 4 3
9 3 2 3

Sample Output-1
4

Sample Input-2
4 2
4 4 4 1
1 1 3 4

Sample Output-2
1


Explanation of Sample Output:

In the first case, the first franchise sold a total of 26 baked goods 
(which is 2 baker's dozens), the second franchise sold a total of 13 baked goods 
(which is 1 baker's dozen), and finally, all franchises together sold 13 baked goods 
on the first day (which is 1 baker's dozen). This totals to 4 baker's dozens.

For the second dataset, no franchises made enough baked goods on their own, but there 
was a single baker's dozen created among them all on the first day. 
This totals to 1 baker's dozen.
'''

def bakerDays(D):
    days_lst = []

    for i in range(D):
        day = input(": ").split()
        for i in range(len(day)):
            day[i] = int(day[i])
        days_lst.append(day)
    return days_lst


def check_13(days_lst, F, D):
    franchise_list = []

    baker_count = 0

    for day in days_lst:
        if sum(day) % 13 == 0:
            baker_count += sum(day) // 13

    for i in range(F):
        for j in range(D):
            franchise_list.append(days_lst[j][i])
        franchise_sum = sum(franchise_list)
        if franchise_sum % 13 == 0:
            baker_count += sum(day) // 13
    
    return baker_count
        

    

# franchises_and_days = input('Enter the number of franchises and the number of days: ').split()

# F = int(franchises_and_days[0])


# D = int(franchises_and_days[1])


# days_lst = bakerDays(D)

# # print(check_13(days_lst, F, D))






'''
Question 4: Unique Paths
Given a m by n matrix, you are to determine and print the 
number of unique paths starting at the top left corner and
ending at the bottom right corner of the matrix.  The only
possible moves that can be made are either a move to the
right or down. 

    Example-1: 

        0  1
    [0   [x, x],
    1   [x, x]  ]

    path 1: (0, 0) --> (0, 1) --> (1, 1)
    path 2: (0, 0) --> (1, 0) --> (1, 1)

    => output: 2


    Example-2: 

        0  1  2
    [0   [x, x, x],
    1   [x, x, x],
    2   [x, x, x]  ]

    path 1: (0, 0) --> (0, 1) --> (0, 2) --> (1, 2)
    path 2: (0, 0) --> (0, 1) --> (1, 1) --> (1, 2)
    path 3: (0, 0) --> (1, 0) --> (1, 1) --> (1, 2)

    => output: 3
    '''

# def matrixPaths(matrix):

#     row = len(matrix)
#     column = len(matrix[0])

#     start = matrix[0][0]

#     end = matrix[-1][-1]

#     for i in range(row):
#         for j in range(column):


def uniquePaths(m, n):
    
    matrix = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]


print(uniquePaths(2, 2))

'''
Question 5: 
Update Pascal's Triangle code so that your algorithm uses only O(1) space.  
'''

# I finished this question

