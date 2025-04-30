# time complexity: O(log(n))
# space complexity:O(1)

# we assume that the list is sorted.

# we can visualize the time complexity with a decision tree


def binarySearch(lst, target):

    nums = lst

    l = 0
    m = 0 
    r = len(nums) - 1


    while l <= r: # if we still have space to search 

        m = (l + r) // 2 # middle value

        if target == nums[m]:
            return m
        elif target > nums[m]: # target is in right half
            l = m + 1
            print(f'Looking for {target} in list {nums[l:r + 1]}')

        elif target < nums[m]: # target is in left half
            r = m - 1
            print(f'Looking for {target} in list {nums[l:m]}')

    return -1 


lst = [3, 5, 7, 8, 9, 10, 12, 14, 17, 19]

num = 17

result = binarySearch(lst, num)

if result != 1:
    print(f'Element {num} is present at index {result}')
else:
    print(f'Element {num} was not found in the list')


'''
< > 

8 -> 2^0
4 12 -> 2^1
2 6 10 14 -> 2^2
1 3 5 7 9 11 13 15 -> 2^3

Four comparisons

Worse case you start from the root and you get to the tree

If you find the height of the three, it's the run time 

The height of the tree is O(log(n))

n = 2^0 + 2^1 + 2^2 + ... + 2^h = 2^h+1 - 1

n = 2^h+1 - 1

n + 1 = 2^h + 1

log(n + 1) = lg(2^h + 1)

log(n + 1) = lg(2) (h + 1)

h = log(n + 1) - 1


log(n + 1) - 1 belongs to O(lgn) 

c n0 for all n >= n0 s.t

lg(n + 1) <= clgn + 1

n + 1 <= n^2

lg(n + 1) <= lg(n^2) + 1

= 2lg(n) + 1

let c = 2 and n0 = 2

proof done


Every node has two children at most 

This is a complete binary tree 

'''