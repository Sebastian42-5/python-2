'''
We are given n unopened boxes with k number of figurines 
in each box. The boxes cannot be opened and hence, 
the order of the figurines cannot be changed. 

A box cannot be rotated (otherwise the figurines would be facing 
the wrong way)

Each figurine is specified by its height. 

For example. In a given height of the figurine from left to right 4, 5, and 7. 

Note that the number of figurines in each box may vary.

We would like to organize all the toy boxes such that they are arranged in 
non-decreasing order of figurine heights from left to right.

However, this may not be necessarily be possible with the given boxes. Hence, write 
a program to determine if we can have such an arrangement or not. 

INPUT SPECIFICATION 

first line of input: integer n n that is representing the number of toy boxes

next n line: oen for each box. Each of these lines begin with the following:

integer k indicating the number of figurines in the box (k >= 1)

Followed by k integers giving the height of figurines from left to right separated by a space

Each height is an integer value >= 1

YES if we can organize the boxes

NO if we can't


Top down design:

It captures the main tasks of your solution

some tasks will not require much code 

will solve them directly

other tasks will require more from us 

will define a function 


'''


# MAIN PROGRAM

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


# TODO : read input 


n = int(input('Number of boxes: '))

boxes = readBoxes(n)


# TODO : check if all the boxes are okay 

if not allBoxesOK(boxes):
    print('NO!')

else:
    # TODO : Obtain a new list of boxes with only the left and right heights (intervals)

    intervals = boxIntervals(boxes)

    # TODO : sort the boxes (the intervals)

    intervals.sort()

    print(intervals)

    # TODO : determine whether the boxes are organized or not 

    if allIntervalsOK(intervals):
        print('YES!')

    else:
        print('NO!')


# TODO : output the result



# def toyBoxes(n, k, h):
#     pass


# number_of_boxes = int(input('Enter the number of boxes: '))

# for i in range(number_of_boxes):
#     toys = input(f'How many toys are in box {i + 1}: ').split()
#     for k in range(toys):
#         height = int(input(f'Enter the height of toy {k + 1}: '))

