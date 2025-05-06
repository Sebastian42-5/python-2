def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2

    left = lst[:mid] # this is creating a copy of the list

    right = lst[mid:] # this too

    sorted_left = mergeSort(left)

    sorted_right = mergeSort(right)

    return merge(sorted_left, sorted_right)



def merge(left, right):
    i = 0 
    j = 0 

    new_lst = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_lst.append(left[i])
            i += 1
        else:
            new_lst.append(right[j])
            j += 1
    
    new_lst.extend(left[i:])
    new_lst.extend(right[j:])

    
    return new_lst

unsorted_lst = [3, 7, 6, -10, -3, 15, 23.5, 55, -13]
sorted_lst = mergeSort(unsorted_lst)


# print(f'Sorted List: {sorted_lst}')



# the runtime for this algorithm is O(nlgn)

# the height of the tree is O(lgn)

# the width is the n in O(nlgn) the n is the recursive call

# the merging process takes linear time


'''
quick sort

in practice, best runtime is O(nlgn) average is O(nlgn) worst is O(n^2)

Quick sort can be better than merge sort 

There are different versions

recursive algorithm 

Step 1: find pivot (slicing) everything that is the pivot gets to the middle

Step 2: Partition your list around the pivot

Step 3: recursive on the left most half and right most half 

Step 4: combine the two lists

Pivot can be chosen different ways 

Deterministic quick sort 

85 24 63 45 17 31 96 50 

The same recursion tree 

The pivot can also be chosen randomly 

Randomized quick sort: best quick sort 

Let's take 50 as the pivot for a deterministic quick sort

50 is the middle 

24 45 17 31 (50) 85 63 96 

recursion

pivot is 31 

24 17 (31) 45

recursion

pivot is 17 

() (17) 24

merge step done 

24

-> 24 itself, it goes back 


17 24 

17 24 31 45 

45

45

< == > 

17 24 34 45 

Another function would do the partition for you

concatenate with the greater than the lesser than 

------------------------------------------------

1. Just make it work
2. inplace: you're limited in space, you change the lst such that the pivot is in the middle
left half is less than pivot, right half is higher than pivot

n 

n/2 n/2 

n/4 n/4 n/4 n/4

O(lgn)

O(nlgn)

Worst case: n, n-1, n-2 ... O(n^2)

If you randomly chose a good pivot, there is a good distribution

'''


def quickSort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[-1]

    left = [] 

    right = [] 

    for i in range(len(lst) - 1):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])


    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort([3, 8, 4, 7, 5, 2, 9, 2, 5, 2, 7]))















